from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Registro.html')
def Entrada(request):
    return render(request, 'Entrada.html')
def Inicio(request):
    return render(request, 'Inicio.html')
