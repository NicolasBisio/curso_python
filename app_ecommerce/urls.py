"""
URL configuration for python_proyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_ecommerce.views import show_index, create_user, show_users, search_users, create_product, show_products, search_products, create_cart, show_carts, search_carts

urlpatterns = [
    path('', show_index),
    path('create_user/', create_user),
    path('show_users/', show_users),
    path('search_users/', search_users),
    path('create_product/', create_product),
    path('show_products/', show_products),
    path('search_products/', search_products),
    path('create_cart/', create_cart),
    path('show_carts/', show_carts),
    path('search_carts/', search_carts),
]