from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.contact, name='product'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forget-password/', views.forget, name='forget'),
]
