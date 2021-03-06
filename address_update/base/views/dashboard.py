from rest_framework import response
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import jwt
import requests
import json
from ..models import RequestForApproval
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.html import strip_tags
from datetime import datetime
from ..models import *
from ..api_functions import *
from ..decorators import *
from django.shortcuts import render,redirect
from itertools import chain
from ..serializers import *

#dashboard apis

#add request
@api_view(['POST'])
@login_required
def create_req(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_aadhar_no = request_data['aadhar_no']
        note = request_data['note']
        user = get_object_from_token(request_data['token'],"_SECRET_KEY")
        print(user)
        user_instance = CustomUser.objects.get(pk=user.get('user_id'))
        request_exists = RequestForApproval.objects.filter(resident=user_instance).filter(final_status__in=['n', 'N'])
        if request_exists:
            return Response({'Message':"One request already exists"},status=status.HTTP_400_BAD_REQUEST)
        else: 
            new_request = RequestForApproval(landlord = landlord_aadhar_no, resident = user_instance, note = note, date_of_request = datetime.now(), landlord_consent="n", final_status="n")
            new_request.save()
            return Response({'Message':"Request has been created"},status=status.HTTP_200_OK)
    else:
        return Response({'Message':"Wrong method"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@landlord_login_required
def landlord_dashboard(request):
    if request.method == 'POST':
        request_data = request.data
        token = request_data['token']
        aadhar_number = get_object_from_token(token,'1234')
        landlord_requests = RequestForApproval.objects.filter(landlord=aadhar_number)
        request_serializer = RequestForApprovalSerializer(landlord_requests,many=True)
        return Response({'Message':'Fetched landlord requests','landlord_requests': request_serializer.data},status = status.HTTP_200_OK)

@api_view(['POST'])
@landlord_login_required
def landlord_request_details(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_request_id = request_data['request_id']
        request_details = RequestForApproval.objects.get(id=landlord_request_id)
        request_serializer = RequestForApprovalSerializer([request_details],many=True)
        return Response({'Message':'Fetched landlord requests', 'request_details': request_serializer.data},status = status.HTTP_200_OK)

@api_view(['POST'])
@landlord_login_required
def handle_request_after_consent(request):
    if request.method == 'POST':
        request_data = request.data
        request_id = request_data['request_id']
        request_approval_status = request_data['request_approval_status']
        request = RequestForApproval.objects.get(id = request_id)
        if request_approval_status == 'SUCCESS':
            request.landlord_consent = 'a'
            request_tenant_id = RequestForApproval.objects.get(pk=request_data['request_id']).resident.id
            address = Address(user = request_tenant_id,
                            landlord_name = 'Partially approved',
                            house = request_data['house'],
                            street =request_data['street'], 
                            landmark =request_data['landmark'], 
                            locality =request_data['locality'], 
                            vtc =request_data['vtc'], 
                            subdist = request_data['subdist'],
                            district = request_data['district'],
                            state = request_data['state'],
                            country = request_data['country'],
                            pincode=request_data['pincode'])
            address.save()
            request.save()            
        elif request_approval_status == "FAIL": 
            request.landlord_consent = 'x'
            request.final_status = 'x'
            request.save()
        
        return Response({'Message':'Landlord consent received'},status = status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def show_requests(request):
    if request.method == "POST":
        data = request.data
        print(data['user_id'])
        current_request = RequestForApproval.objects.filter(resident = data["user_id"],final_status='n')
        previous_approved_requests = RequestForApproval.objects.filter(resident = data["user_id"],final_status = 'a')
        previous_rejected_requests = RequestForApproval.objects.filter(resident = data["user_id"],final_status = 'x')
        previous_requests = chain(previous_approved_requests,previous_rejected_requests)

        current_request_serializer = RequestForApprovalSerializer(current_request,many=True)
        previous_requests_serializer = RequestForApprovalSerializer(previous_requests,many=True)

        return Response({'Message':"Requests are fetched","current_request":current_request_serializer.data,
        "previous_requests":previous_requests_serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def delete_request(request):
    if request.method == "POST":
        data = request.data
        req_to_be_deleted = RequestForApproval.objects.get(pk=data["request_id"])
        req_to_be_deleted.delete()
        return Response({'Message':"Request has been deleted"},status=status.HTTP_200_OK)

# to take otp common
@api_view(['POST'])
@login_required
def get_otp(request):
    if request.method == "POST":
        data = request.data
        aadhar_no = data["aadhar_no"]
        otp_response = otp(aadhar_no)

        if otp_response['status'].lower() == "y":
            return Response({'Message':"OTP created",'txnID':otp_response['txnID']},status=status.HTTP_200_OK)
        else:
            return Response({'Message':"Failed to create OTP","error_code":otp_response["error_code"]},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_token_for_otp(request):
    if request.method == "POST":
        request_data = request.data
        response = eKyc(request_data['uid'], request_data['otp'], request_data['txn_id'])
        if response.get('status').lower() == 'n':
            return Response({'Message': 'OtpAuthentication Failure','ErrorCode': response['errCode']},status=status.HTTP_400_BAD_REQUEST) 
        else:
            token = get_token_from_object({'uid':request_data['uid']},'1234')
            return Response({'Message':"Token has been generated",'token':token, 'name': response['aadhar_holder_name']},status=status.HTTP_200_OK)
    else:
        return Response({'Error':"Wrong method"},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def authenticate_adderess(request):
    if request.method == "POST":
        request_data = request.data
        tenant_address = request_data['tenant_address'] # in dict format
        landlord_address = request_data['landlord_address'] # in dict format
        tenant_device_gps_address = request_data['tenant_device_gps_address'] # tuple with (lat, lon)
        # aadhar_landlord = get_object_from_token(request.headers['Authorization'], '1234')
        # aadhar_landlord = aadhar_landlord['uid']
        # landlord_address = RequestForApproval.objects.get(landlord=aadhar_landlord)
        valid = validate_address(tenant_address,landlord_address,tenant_device_gps_address,string_threshold_level=6,km_threshold_level=0.5)
        if valid:
            # send updated address to UIDAI
            print(landlord_address)
            address = Tenant_Approved_Address(user = request_tenant_id,
                            landlord_name = 'Partially approved',
                            house = landlord_address['house'],
                            street =landlord_address['street'], 
                            landmark =landlord_address['landmark'], 
                            locality =landlord_address['locality'], 
                            vtc =landlord_address['vtc'], 
                            subdist = landlord_address['subdist'],
                            district = landlord_address['district'],
                            state = landlord_address['state'],
                            country = landlord_address['country'],
                            pincode=landlord_address['pincode'])
            address.save()
        else:
            return Response({'Message':"Major Changes detected in Address. Not Approved"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Error':"Wrong method"},status=status.HTTP_400_BAD_REQUEST)