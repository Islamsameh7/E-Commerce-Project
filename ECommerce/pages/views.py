from json import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import render
from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from pages.models import Product
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth import logout


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def product(request):
    return render(request, 'pages/product.html')

def logout_view(request):
    logout(request)
    return render(request, 'pages/home.html')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if request.user.is_superuser:
            return redirect('/admin/')
        
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User is not found')
            return redirect('/login')

        profile_obj = Profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(
                request, 'this account is not activated , please check your mail')
            return redirect('/login')

        if profile_obj.suspended:
            messages.success(request, 'this account has been suspended')
            return redirect('/login')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong credintials')
            return redirect('/login')

        login(request, user)
        return redirect('/')

    return render(request, 'pages/login.html')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        phone_number = request.POST.get('mobile')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'username is taken !')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'email is taken !')
                return redirect('/register')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(
                user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_activation_mail(email, auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request, 'pages/registeration.html')


def success(request):
    return render(request, 'pages/success.html')


def token_send(request):
    return render(request, 'pages/token.html')


def send_activation_mail(email, token):
    subject = "Your acoount needs to be verified"
    message = f'please click the following link to verify your account: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already activated')
                return redirect('/login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been activated')
            return redirect('/login')

        else:
            return redirect('/error')

    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'pages/error.html')


def forgot_password_error(request):
    return render(request, 'pages/forgot_password_error.html')


def forgot_password(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        try:
            if User.objects.filter(email=email).first():
                user = User.objects.get(email=email)
                password = User.objects.make_random_password()
                user.set_password(password)
                user.save()
                subject = "username and password"
                message = f'username is: {user.username} ,, password is: {password}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(
                    request, 'check your email for account credintials')
                return redirect('/login')

            else:
                return redirect('/forgot_password_error')

        except Exception as e:
            print(e)

    return render(request, 'pages/forgot_password.html')


def shop(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems= order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}

    return render(request, 'pages/shop.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems= order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'pages/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems= order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'pages/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productName = data['productName']
    action = data['action']

    print('Action: ', action)
    print('Product name: ', productName)

    customer = request.user.customer
    product = Product.objects.get(name=productName)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in..')
    return JsonResponse('Payment complete!', safe=False)