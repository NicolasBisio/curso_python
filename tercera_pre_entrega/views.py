from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def saludo_render(request):
    context = {}
    return render(request, "index.html", context)