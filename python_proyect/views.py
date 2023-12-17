from django.shortcuts import render

def show_index(request):
    return render(request, "pages/index.html")

def about_me(request):
    return render(request, "pages/about_me.html")

def error_404(request, exception):
    return render(request, '404.html', {'mensaje': "La página que buscas no existe."}, status=404)