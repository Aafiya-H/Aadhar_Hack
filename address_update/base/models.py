from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField()
    aadhar_no = models.CharField(max_length=12)
    name = models.TextField()

class RequestForApproval(models.Model):
    landlord = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    resident = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    note = models.TextField()

    landlord_consent = models.CharField(max_length = 1) 
    final_status = models.CharField(max_length = 1)
    # n - not decided
    # a - approved
    # x - not approved

    date_of_request = models.DateField()
    date_of_approval = models.DateField()


class Supporting_Document(models.Model):
    request = models.ForeignKey(RequestForApproval,on_delete = models.CASCADE)
    document_url = models.TextField()
    document_name = models.TextField()


class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE) 
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
