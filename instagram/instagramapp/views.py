from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
# Create your views here.

def index(request):
    return render(request, 'Registro.html')
def crear_usuario(request):
    _email = request.POST['email']
    _username = request.POST['username']
    _password = request.POST['password']
    _name = request.POST['name']
    print (_email)
    print (_username)
    print (_password)
    print (_name)
    user=User.objects.create_user( username = _username, email =_email, first_name =_name, password =_password  )
    myUser = MiUsuario( usuario = user )
    myUser.save()
    print (user)
    print (user.password)
    return redirect('Entrada')
def Entrada(request):
    return render(request, 'Entrada.html')
def Inicio(request):
    return render(request, 'Inicio.html')
def Perfil(request):
    return render(request, 'Perfil.html')
