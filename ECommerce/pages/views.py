from django.shortcuts import render

from pages.models import Product


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def shop(request):
    products = Product.objects.all()
    context ={'products':products}
    
    return render(request, 'pages/shop.html' , context)
    