from django.shortcuts import render
from .models import Producto

def home (request):
    return render(request, 'core/home.html')

def boleta(request):
    return render (request,'core/boleta.html')

def catalogo(request):
    listado_prod = Producto.objects.all()
    data = {"lista" : listado_prod}
    return render (request,'core/catalogo.html',data)

def login(request):
    return render (request,'core/login.html')

def pago(request):
    return render (request,'core/pago.html')

def recuperar_contrasena(request):
    return render (request,'core/recuperar_contrasena.html')

def registro(request):
    return render (request,'core/registro.html')

def ventas(request):
    return render (request,'core/ventas.html')

def carrito(request):
    return render (request,'core/carrito.html')
