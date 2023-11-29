from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_ecommerce.models import User
from app_ecommerce.forms import User_Form, User_Form_Search

# Users Views
def create_user(request):
    if request.method == "POST":
        
        user = User_Form(request.POST)
        if user.is_valid():
            data = user.cleaned_data
            new_user = User(name = data["name"], last_name = data["last_name"], email = data["email"])
            new_user.save()
            return redirect("/app/show_users/")

    user_form = User_Form()
    context = {
        "form": user_form
    }
    return render(request, "app_ecommerce/create_user.html", context)

def show_users(request):
    users = User.objects.all()
    context = {
        "users": users,
        "form": User_Form_Search(),
    }

    return render(request, 'app_ecommerce/users.html', context)

def search_users(request):
    name = request.GET["name"]
    users = User.objects.filter(name__icontains=name)
    context = {
        "users": users,
        "form": User_Form_Search(),
    }
    return render(request, "app_ecommerce/users.html", context)

# Products Views




# Carts Views