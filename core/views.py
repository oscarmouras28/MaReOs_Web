from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Producto, Venta, Vendedor, Cliente, Delivery, Medio_pago, Carrito


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
    delivery = Delivery.objects.all()
    data = {"listaDelivery": delivery}

    if request.POST:
        deliveryAdd = Delivery()
        deliveryAdd.direccion = request.POST.get("direccionDelivery")
        deliveryAdd.telefono = request.POST.get("telefonoDelivery")
        deliveryAdd.valor = request.POST.get("valorDelivery")
        
        cliente = Cliente()
        cliente.id = request.POST.get("idCli")

        deliveryAdd.cliente_id = cliente 
        try:
            deliveryAdd.save()
            mensaje = "Delivery agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar al Delivery"
            messages.Error(request, mensaje)

    return render(request, 'core/pago.html', data)


def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')


def registro(request):
    if request.POST:
        cliente = Cliente()
        cliente.p_nombre = request.POST.get("nombreCli")
        cliente.a_paterno = request.POST.get("apellidoCli")
        cliente.num_contac = request.POST.get("inputTelefono")
        cliente.rut = request.POST.get("rutCli")
        try:
            cliente.save()
            mensaje = "Cliente agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar al Cliente"
            messages.Error(request, mensaje)
    return render(request, 'core/registro.html')


def ventas(request):
    listado_ventas = Venta.objects.all()
    delivery = Delivery.objects.all()
    medioPago = Medio_pago.objects.all()
    data = {"listaVentas": listado_ventas,
            "delivery": delivery,
            "medioPago": medioPago}
    return render(request, 'core/ventas.html', data)


def carrito(request):
    lista_carrito = Carrito.objects.all()
    data = {"listaCarrito": lista_carrito}
    return render(request, 'core/carrito.html', data)


def agregar_vendedor(request):
    # guardar
    if request.POST:
        vendedor = Vendedor()
        vendedor.p_nombre = request.POST.get("primNombre")
        vendedor.s_nombre = request.POST.get("segNombre")
        vendedor.a_paterno = request.POST.get("apPaterno")
        vendedor.a_materno = request.POST.get("apMaterno")
        vendedor.rut = request.POST.get("txtRut")

        try:
            vendedor.save()
            mensaje = "Vendedor agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar al vendedor"
            messages.Error(request, mensaje)

    return render(request, 'core/agregar_vendedor.html')


def ver_vendedores(request):
    listado_Vendedores = Vendedor.objects.all()
    data = {"listaVendedores": listado_Vendedores}
    return render(request, 'core/ver_vendedores.html', data)


def ver_clientes(request):
    listado_clientes = Cliente.objects.all()
    data = {"listaClientes": listado_clientes}
    return render(request, 'core/ver_clientes.html', data)


def agregarProducto(request):
    if request.POST:
        producto = Producto()
        producto.nombre = request.POST.get("prodNombre")
        producto.precio = request.POST.get("precioProd")
        producto.img = request.POST.get("txtImagen")
        producto.desc = request.POST.get("descProd")
        producto.tip_producto = request.POST.get("tipoProd")
        try:
            producto.save()
            mensaje = "Producto agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar el Producto"
            messages.Error(request, mensaje)
    return render(request, 'core/agregar_producto.html')


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


def ver_pagos(request):
    listaPagos = Medio_pago.objects.all()
    data = {"listaMediosPagos": listaPagos}
    return render(request, 'core/ver_tipos_pago.html', data)


def agregarmedioPago(request):
    if request.POST:
        medio_pago = Medio_pago()
        medio_pago.tipo_pago = request.POST.get("medioPago")

        try:
            medio_pago.save()
            mensaje = "Medio de Pago agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar el Medio de pago"
            messages.Error(request, mensaje)
    return render(request, 'core/agregar_medioPago.html')


def eliminarCli(request, id):
    cliente = Cliente.objects.get(id=id)

    try:
        cliente.delete()
        mensaje = "Cliente eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar al Cliente"
        messages.Error(request, mensaje)

    return redirect('ver_clientes')


def eliminarVen(request, id):
    vendedor = Vendedor.objects.get(id=id)

    try:
        vendedor.delete()
        mensaje = "Vendedor eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar al Vendedor"
        messages.Error(request, mensaje)

    return redirect('ver_vendedores')


def eliminarProd(request, id):
    producto = Producto.objects.get(id=id)

    try:
        producto.delete()
        mensaje = "Producto eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar el Producto"
        messages.Error(request, mensaje)

    return redirect('ver_productos')


def eliminarVenta(request, id):
    venta = Venta.objects.get(id=id)

    try:
        venta.delete()
        mensaje = "Venta eliminada"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar la Venta"
        messages.Error(request, mensaje)

    return redirect('ventas')


def eliminarMedioPago(request, id):
    medioPago = Medio_pago.objects.get(id=id)

    try:
        medioPago.delete()
        mensaje = "Medio de Pago eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar medio de pago"
        messages.Error(request, mensaje)

    return redirect('ver_medios_pago')


def eliminarMiDelivery(request, id):
    miDelivery = Delivery.objects.get(id=id)

    try:
        miDelivery.delete()
        mensaje = "Delivery eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar Delivery"
        messages.Error(request, mensaje)

    return redirect('pago')
