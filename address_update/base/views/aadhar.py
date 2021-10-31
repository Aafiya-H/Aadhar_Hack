from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import CustomUser
from ..serializers import UserSerializer
from ..decorators import get_object_from_token, get_token_from_object, login_required
import jwt
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.html import strip_tags
from ..api_functions import *


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