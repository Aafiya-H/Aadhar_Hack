from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf  import settings

class CustomUser(AbstractUser):
    email = models.EmailField()
    aadhar_no = models.CharField(max_length=12)
    name = models.TextField()


class RequestForApproval(models.Model):
    landlord = models.CharField(max_length = 12)
    resident = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "resident")
    note = models.TextField()

    landlord_consent = models.CharField(max_length=1)
    final_status = models.CharField(max_length=1)
    # n - not decided
    # a - approved
    # x - not approved

    date_of_request = models.DateField()
    date_of_approval = models.DateField(null=True)
    


class Supporting_Document(models.Model):
    request = models.ForeignKey(RequestForApproval, on_delete=models.CASCADE)
    document_url = models.TextField()
    document_name = models.TextField()


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    landlord_name = models.TextField(default="")
    house = models.TextField()
    street = models.TextField()
    landmark = models.TextField()
    locality = models.TextField()
    vtc = models.TextField()
    subdist = models.TextField()
    district = models.TextField()
    state = models.TextField()
    country = models.TextField()
    pincode = models.CharField(max_length = 6)

class Tenant_Approved_Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    landlord_name = models.TextField(default="")
    house = models.TextField()
    street = models.TextField()
    landmark = models.TextField()
    locality = models.TextField()
    vtc = models.TextField()
    subdist = models.TextField()
    district = models.TextField()
    state = models.TextField()
    country = models.TextField()
    pincode = models.CharField(max_length = 6)


# Create your models here.
