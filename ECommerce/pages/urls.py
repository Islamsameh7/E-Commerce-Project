from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('product', product, name='product'),
    path('login', login_attempt, name="login"),
    path('register', register_attempt, name="register"),
    path('token',token_send, name = "token"),
    path('success',success, name = "success"),
    path('verify/<auth_token>' , verify, name = "verify"),
    path('error' , error_page , name ="error"),
    path('forgot_password', forgot_password, name="forgot_password"),
    path('forgot_password_error', forgot_password_error, name="forgot_password_error"),
    path('update_item', updateItem, name="update_item"),

]
