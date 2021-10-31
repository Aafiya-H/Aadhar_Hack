from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class Supporting_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporting_Document
        fields = '__all__'

class RequestForApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForApproval
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'