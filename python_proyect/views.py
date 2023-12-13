from django.shortcuts import render

def show_index(request):
    return render(request, "pages/index.html")

def about_me(request):
    return render(request, "pages/about_me.html")