from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
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
    return redirect('Login')

@login_required
def Subir(request):
    return render(request, 'Subir.html')
@login_required
def Inicio(request):
    return render(request, 'Inicio.html')
@login_required
def Perfil(request):
    curr_user = request.user
    mi_usuario = MiUsuario.objects.get(pk = curr_user.id)
    media_user = Post.objects.filter( creador = mi_usuario );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'Perfil.html', context)

@login_required
def uploadFile (request):
    curr_user = request.user
    mi_usuario = MiUsuario.objects.get(pk = curr_user.id)
    post_user = Post.objects.filter(creador=curr_user.id).count()
    mediaFile = request.FILES['photo']
    newNameFile= curr_user.username + "-" + str(curr_user.id) + "-" +str(post_user)
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = "";
    newPost = Post( foto = photo, descripcion = description, creador = mi_usuario );
    newPost.save();
    media_user = Post.objects.filter( creador = mi_usuario );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'Perfil.html', context)
