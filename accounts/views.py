from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import AvatarUpdateForm, UserRegisterForm, UserUpdateForm
from accounts.models import Avatar

# Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

        return redirect('/app/show_products/')

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

# Register
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/accounts/login/")

    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)

# Update
@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":

        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.save()
            return redirect("/app/show_products/")

    form = UserUpdateForm(initial={"email": user.email})
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)

@login_required
def user_update_avatar(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("/app/show_products/")

    form = AvatarUpdateForm()
    context = {
        "form": form
    }
    return render(request, "accounts/avatar.html", context)