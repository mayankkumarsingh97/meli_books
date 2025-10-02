from django.db import models
from django.contrib.auth.models import User
#
#
# Create your models here.
#
#
class Profile(models.Model):
    OPTIONS = (
    ('1','None'),
     ('Yes' , 'Yes'),
     ('No' , 'No')
     )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="profile")
    name = models.CharField(max_length=200, null=False, blank=False,verbose_name="Full Name")
    email = models.CharField(max_length=200, null=False, unique=True,  blank=False,verbose_name="Email")
    phone = models.CharField(max_length=20, null=True,  blank=False,verbose_name="Phone")
    company_name = models.CharField(max_length=200, null=True,blank=True,verbose_name="Company Name")
    company_address = models.CharField(max_length=200, null=True,blank=True,verbose_name="Company Address")
    country = models.CharField(max_length=200, null=True,blank=True,verbose_name="Country")
    business_nature = models.CharField(max_length=200, null=True,blank=True,verbose_name="Business Nature")
    business_type = models.CharField(max_length=200, null=True,blank=True,verbose_name="Business Type")
    business_duration = models.CharField(max_length=200, null=True, blank=True,verbose_name="Duration of Business")
    agreement = models.CharField(max_length=200, null=True,blank=True,verbose_name="Minimum Amount Invest Starting At")
    website_link = models.CharField(max_length=200,blank=True,null=True,verbose_name="Website Link")
    licence = models.FileField(upload_to='licence/',verbose_name="Cosmetologist Licence", blank=True)
    trial = models.BooleanField(default=True, blank=True,verbose_name="On Trial")
    approved = models.CharField(max_length=20,blank=True,default='blank',verbose_name="Approval")

    def __str__(self):
        return str(self.email)
