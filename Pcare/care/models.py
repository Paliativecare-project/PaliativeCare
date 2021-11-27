from django.db import models


# Create your models here.
class User(models.Model):
    u_id=models.IntegerField()
    u_name=models.CharField(max_length=255)
    u_email=models.EmailField((""), max_length=254)
    u_phn=models.IntegerField()
    u_address=models.CharField(max_length=255)
    u_password=models.CharField(max_length=16)  
    
    
    def __str__(self):
      return self.u_name
class Service(models.Model):
    name=models.CharField(max_length=100,blank=False)
    addr=models.CharField(max_length=100,blank=False)
    phn=models.IntegerField()
    distric=models.CharField(max_length=100,blank=False)
    pincode=models.IntegerField(blank=False)
    email=models.EmailField(max_length=70,blank=False)
    password=models.CharField(max_length=70,blank=False)

    def __str__(self):
        return self.name
 