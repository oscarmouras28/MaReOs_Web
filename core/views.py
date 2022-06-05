from django.shortcuts import render
from .models import Producto, Venta, Vendedor, Cliente, Delivery, Medio_pago


def home(request):
    return render(request, 'core/home.html')


def boleta(request):
    listado_ventas = Venta.objects.all()
    delivery = Delivery.objects.all()
    data = {"listaVentas": listado_ventas,
            "delivery": delivery}
    return render(request, 'core/boleta.html', data)


def catalogo(request):
    listado_sandwich = Producto.objects.filter(tip_producto='1')
    listado_para_picar = Producto.objects.filter(tip_producto='2')
    listado_completo = Producto.objects.filter(tip_producto='3')
    listado_agregados = Producto.objects.filter(tip_producto='4')

    data = {"listaSandiwch": listado_sandwich,
            "listaParaPicar": listado_para_picar,
            "listaCompleto": listado_completo,
            "listaAgregados": listado_agregados}

    return render(request, 'core/catalogo.html', data)


def login(request):
    return render(request, 'core/login.html')


def pago(request):
    return render(request, 'core/pago.html')


def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')


def registro(request):
    return render(request, 'core/registro.html')


def ventas(request):
    listado_ventas = Venta.objects.all()
    delivery = Delivery.objects.all()
    medioPago = Medio_pago.objects.all()
    data = {"listaVentas": listado_ventas,
            "delivery" : delivery,
            "medioPago" : medioPago}
    return render(request, 'core/ventas.html', data)


def carrito(request):
    return render(request, 'core/carrito.html')


def ver_vendedores(request):
    listado_Vendedores = Vendedor.objects.all()
    data = {"listaVendedores": listado_Vendedores}
    return render(request, 'core/ver_vendedores.html', data)


def ver_clientes(request):
    listado_clientes = Cliente.objects.all()
    data = {"listaClientes": listado_clientes}
    return render(request, 'core/ver_clientes.html', data)


def ver_productos(request):
    listado_sandwich = Producto.objects.filter(tip_producto='1')
    listado_para_picar = Producto.objects.filter(tip_producto='2')
    listado_completo = Producto.objects.filter(tip_producto='3')
    listado_agregados = Producto.objects.filter(tip_producto='4')

    data = {"listaSandwich": listado_sandwich,
            "listaParaPicar": listado_para_picar,
            "listaCompleto": listado_completo,
            "listaAgregados": listado_agregados}
    return render(request, 'core/ver_productos.html', data)