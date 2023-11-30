from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_ecommerce.models import User, Product, Cart
from app_ecommerce.forms import User_Form, User_Form_Search, Product_Form, Product_Form_Search, Cart_Form, Cart_Form_Search

# Index
def show_index(request):
    return render(request, "app_ecommerce/index.html")

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
def create_product(request):
    if request.method == "POST":
        
        product = Product_Form(request.POST)
        if product.is_valid():
            data = product.cleaned_data
            new_product = Product(title = data["title"], price = data["price"])
            new_product.save()
            return redirect("/app/show_products/")

    product_form = Product_Form()
    context = {
        "form": product_form
    }
    return render(request, "app_ecommerce/create_product.html", context)

def show_products(request):
    products = Product.objects.all()
    context = {
        "products": products,
        "form": Product_Form_Search(),
    }

    return render(request, 'app_ecommerce/products.html', context)

def search_products(request):
    title = request.GET["title"]
    products = Product.objects.filter(title__icontains=title)
    context = {
        "products": products,
        "form": Product_Form_Search(),
    }
    return render(request, "app_ecommerce/products.html", context)

# Carts Views
def create_cart(request):
    if request.method == "POST":
        
        cart = Cart_Form(request.POST)
        if cart.is_valid():
            data = cart.cleaned_data
            new_cart = Cart(cart_user = data["cart_user"], products = data["products"], total = data["total"])
            new_cart.save()
            return redirect("/app/show_carts/")

    cart_form = Cart_Form()
    context = {
        "form": cart_form
    }
    return render(request, "app_ecommerce/create_cart.html", context)

def show_carts(request):
    carts = Cart.objects.all()
    context = {
        "carts": carts,
        "form": Cart_Form_Search(),
    }

    return render(request, 'app_ecommerce/carts.html', context)

def search_carts(request):
    cart_user = request.GET["cart_user"]
    carts = Cart.objects.filter(cart_user__icontains=cart_user)
    context = {
        "carts": carts,
        "form": Cart_Form_Search(),
    }
    return render(request, "app_ecommerce/carts.html", context)