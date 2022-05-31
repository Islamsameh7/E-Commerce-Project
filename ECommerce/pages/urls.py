from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact_us', contact_us, name='contact_us'),
    path('product', product, name='product'),
    path('login', login_attempt, name="login"),
    path('register', register_attempt, name="register"),
    path('delete_user', delete_user, name="delete_user"),
    path('token',token_send, name = "token"),
    path('success',success, name = "success"),
    path('verify/<auth_token>' , verify, name = "verify"),
    path('error' , error_page , name ="error"),
    path('forgot_password', forgot_password, name="forgot_password"),
    path('forgot_password_error', forgot_password_error, name="forgot_password_error"),
    path('update_item', updateItem, name="update_item"),
    path('process_order', processOrder, name="process_order"),
    path('home', logout_view, name="logout"),
    path('profile', profile, name="profile"),
    path('update_profile', updateProfile, name="update_profile"),
    path('charts', charts, name="charts"),
    path('pie_chart', pie_chart, name="pie_chart"),
    path('bar_chart', bar_chart, name="bar_chart"),
    path('gender_chart', gender_chart, name="gender_chart"),
    path('change_pass', ChangePasswordView.as_view(), name='change_pass'),
    

]
