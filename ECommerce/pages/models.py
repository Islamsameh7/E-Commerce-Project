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
    
class Order(models.Model):   
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank = True,null=True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False, null=True , blank= True)  
    transaction_id = models.CharField(max_length=200, null = True)
    
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):   
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,blank = True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank = True,null=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price *self.quantity
        return total

class ShippingAddress(models.Model): 
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank = True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank = True,null=True)  
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)    
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
        
    
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    auth_token = models.CharField(max_length=100 )
    suspended = models.BooleanField(default = False)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
# Create your models here.
