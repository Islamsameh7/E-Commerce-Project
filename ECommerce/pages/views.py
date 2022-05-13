from django.shortcuts import render

from pages.models import Product


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def shop(request):
    products = Product.objects.all()
    context ={'products':products}
    
    return render(request, 'pages/shop.html' , context)
    
def about(request):
    return render(request, 'pages/about.html')

def cart(request):
    return render(request, 'pages/cart.html')

def contact(request):
    return render(request, 'pages/contact.html')

def product(request):
    return render(request, 'pages/product.html')

def register(request):
    return render(request, 'pages/registeration.html')

def login(request):
    return render(request, 'pages/login.html')

def forget(request):
    return render(request, 'pages/forget_password.html')