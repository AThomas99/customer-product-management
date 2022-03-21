from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='product'),
    path('customer/<str:pk>/', views.customers, name='customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create-order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete-order'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
