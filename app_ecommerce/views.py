from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_ecommerce.models import User

def create_user(request):
    new_user = User(name = "Lionel", last_name = "Messi", email = "lio10@gmail.com")
    new_user.save()

    context = {
        "nombre": new_user.name
        }

    return render(request, "index.html", context)