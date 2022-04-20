from django.shortcuts import render
def home(request):
    return render(request,'core/home.html')
def login(request):
    return render(request,'core/login.html')
def pago(request):
    return render(request,'core/pago.html')
def registro(request):
    return render(request,'core/registro.html')
def recuperarContraseña(request):
    return render(request,'core/recuperarContraseña.html')
def ventas(request):
    return render(request,'core/ventas.html')
def catalogo(request):
    return render(request,'core/catalogo.html')
def boleta(request):
    return render(request,'core/boleta.html')
# Create your views here.
