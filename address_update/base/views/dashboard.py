from rest_framework import response
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import jwt
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.html import strip_tags
from ..models import *
from ..api_functions import *
from ..decorators import login_required
from django.shortcuts import render,redirect
from itertools import chain
from ..serializers import *

#dashboard apis

#add request
@api_view(['POST'])
def create_req(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_aadhar_no = request_data['aadhar_no']
        note = request_data['note']

        return Response({'Message':"Request has been created"},status=status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def show_requests(request):
    if request.method == "POST":
        data = request.data
        current_request = RequestForApproval.objects.get(resident = data["user_id"],final_status='n')
        previous_approved_requests = RequestForApproval.objects.filter(resident = data["user_id"],final_status = 'a')
        previous_rejected_requests = RequestForApproval.objects.filter(resident = data["user_id"],final_status = 'x')
        previous_requests = chain(previous_approved_requests,previous_rejected_requests)

        current_request_serializer = RequestForApprovalSerializer(current_request)
        previous_requests_serializer = RequestForApprovalSerializer(previous_requests,many=True)

        return Response({'Message':"User has been created","current_request":current_request_serializer.data,
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

        
