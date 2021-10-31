import jwt
from rest_framework.response import Response
from rest_framework import status


def get_object_from_token(token,secret_key):
    return jwt.decode(token, secret_key, algorithms=["HS256"])

def get_token_from_object(token,secret_key):
    return jwt.encode(token, secret_key, algorithm="HS256")

def login_required(function):
    def wrapper(request, *args, **kw):
        try:
            if 'Authorization' in request.headers:
                obj = get_object_from_token(request.headers['Authorization'], '_SECRET_KEY')
                if obj and obj.get('user_id'):
                    print("Token aya")
                    return function(request, *args, **kw)
            else:
                print("Token nahi aya")
                return Response({'Error':"Invalid token"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print("Token is invalid")
            print(e)
            return Response({'Error':"Invalid token"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper

def landlord_login_required(function):
    def wrapper(request, *args, **kw):
        try:
            if 'Authorization' in request.headers:
                print(request.headers['Authorization'])
                obj = get_object_from_token(request.headers['Authorization'], '1234')
                if obj and obj.get('uid'):
                    print("Token aya")
                    return function(request, *args, **kw)
            else:
                print("Token nahi aya")
                return Response({'Error':"Invalid token"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print("Token is invalid")
            print(e)
            return Response({'Error':"Invalid token"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper