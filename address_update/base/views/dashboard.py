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
from ..serializers import *
from ..decorators import *
#dashboard apis

#add request
@api_view(['POST'])
@login_required
def create_req(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_aadhar_no = request_data['aadhar_no']
        note = request_data['note']

        return Response({'Message':"Request has been created"},status=status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def landlord_dashboard(request):
    if request.method == 'POST':
        request_data = request.data
        token = request_data['token']
        aadhar_number = get_object_from_token(token,'1234')
        landlord_requests = RequestForApproval.objects.get(landlord=aadhar_number)
        request_serializer = RequestForApprovalSerializer(landlord_requests,many=True)
        return Response({'Message':'Fetched landlord requests',landlord_requests = request_serializer.data},status = status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def landlord_request_details(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_request_id = request_data['request_id']
        request_details = RequestForApproval.objects.get(id=landlord_request_id)
        request_serializer = RequestForApprovalSerializer([request_details],many=True)
        return Response({'Message':'Fetched landlord requests',request_details = request_serializer.data},status = status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def handle_request_after_consent(request):
    if request.method == 'POST':
        request_data = request.data
        request_id = request_data['request_id']
        request_approval_status = request_data['request_id']
        request = RequestForApproval.objects.get(id = request_id)
        if request_approval_status == 'SUCCESS':
            request.landlord_consent = 'a'
            request_tenant_id = RequestForApproval.objects.get(pk=request_data['request_id']).resident.id
            address = Address(user = request_tenant_id,landlord_name = 'Partially approved'
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
            request.landlord_consent = 'n'
            request.save()
        
        return Response({'Message':'Landlord consent received'},status = status.HTTP_200_OK)