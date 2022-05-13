from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200 ,  null =True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True , blank= False)
    image = models.ImageField(null = True , blank = True)
    
    def __str__(self) :
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    suspended = models.BooleanField(default = False)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username     
# Create your models here.
