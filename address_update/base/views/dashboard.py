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


#dashboard apis

#add request
@api_view(['POST'])
def create_req(request):
    if request.method == 'POST':
        request_data = request.data
        landlord_aadhar_no = request_data['aadhar_no']
        note = request_data['note']

        return Response({'Message':"Request has been created"},status=status.HTTP_200_OK)
