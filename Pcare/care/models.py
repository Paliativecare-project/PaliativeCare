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


        
 