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
import time
from ..api_functions import eKyc

#dashboard apis

#add request
@api_view(['POST'])
def create_req(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_aadhar_no = request_data['aadhar_no']
        note = request_data['note']
        # get user 
        user = get_object_from_token(request_data['token'],"_SECRET_KEY")
        request_exists = RequestForApproval.objects.filter(resident=user).filter(final_status__in=['n', 'N'])
        if request_exists:
            return Response({'Message':"One request already exists"},status=status.HTTP_400_BAD_REQUEST)
        else: 
            new_request = RequestForApproval(landlord = landlord_aadhar_no, resident = username, note = note, date_of_request = datetime.now())
            new_request.save()
            return Response({'Message':"Request has been created"},status=status.HTTP_200_OK)
    else:
        return Response({'Message':"Wrong method"},status=status.HTTP_400_BAD_REQUEST)

#landlord Otp verification and getting kyc details while giving consent
@api_view(['POST'])
def getkyc(request):
    if request.method == 'POST':
        data = request.data
        response = eKyc(data['otp'],data['uid'],data['txn_id'])
        if response.get('Status').lower() == 'n':
            return Response({'Message': 'OtpAuthentication Failure','ErrorCode':res['errCode']},status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response({'Message': 'OtpAuthentication Passed','Address': response.get('address_dict')},status=status.HTTP_200_OK) 
    else:
		return Response({'Error':"Wrong method"},status=status.HTTP_400_BAD_REQUEST)