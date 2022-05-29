from django.contrib import admin
from pages.models import *

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Profile)
admin.site.register(Category)
# Register your models here.
