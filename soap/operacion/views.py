from django.shortcuts import render




from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request, 'operacion/home.html')


def contacto(request):
    return render (request, 'operacion/contacto.html')
