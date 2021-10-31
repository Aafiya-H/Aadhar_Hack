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

@api_view(['POST'])
def fetch_eKYC(request):
    if request.method == 'POST':
        request_data = request.data
        ekyc_response = eKyc(request_data['uid'],request_data['otp'],request_data['txn_id'])
        if ekyc_response['status'].lower() == y:
            return Response({'Message':'Landlord consent received',address_dict = ekyc_response['address_dict']},status = status.HTTP_200_OK)
        return Response({'Message':'Could not fetch eKYC'},status = status.HTTP_200_OK)