from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from .models import Producto, Venta, Vendedor, Cliente, Delivery, Medio_pago, Carrito
from .forms import CustomUserCreationForm

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

def pago(request):
    delivery = Delivery.objects.all()
    pagos = Medio_pago.objects.all()
    data = {"listaDelivery": delivery,
            "listaPagos" : pagos}

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
            messages.error(request, mensaje)

    return render(request, 'core/pago.html', data)

def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')

def registro(request): 
    data ={
        'form': CustomUserCreationForm
    }

    if request.POST:
        formulario=CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect("home")
        
        data["form"] = formulario
    return render(request, 'registration/registro_user.html', data)

def registro_cliente(request):
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
            messages.error(request, mensaje)
    return render(request, 'core/registro.html')


def registro_vendedor(request):
    data ={
        'form': CustomUserCreationForm
    }
    if request.POST:
        vendedor = Vendedor()
        vendedor.p_nombre = request.POST.get("primNombre")
        vendedor.s_nombre = request.POST.get("segNombre")
        vendedor.a_paterno = request.POST.get("apPaterno")
        vendedor.a_materno = request.POST.get("apMaterno")
        vendedor.rut = request.POST.get("txtRut")
        vendedor.username = formulario.cleaned_data["username"]

        try:
            vendedor.save()
            mensaje = "Vendedor agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar al vendedor"
            messages.error(request, mensaje)
    return render(request, 'core/registro_vendedor.html', data)

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
            messages.error(request, mensaje)

    return render(request, 'core/agregar_vendedor.html')

def modificarVendedor(request, id):

    vendedor = Vendedor.objects.get(id=id)

    data = {
        "vendedor" : vendedor
    }

    # modificar
    if request.POST:
        vendedor.p_nombre = request.POST.get("primNombre")
        vendedor.s_nombre = request.POST.get("segNombre")
        vendedor.a_paterno = request.POST.get("apPaterno")
        vendedor.a_materno = request.POST.get("apMaterno")
        vendedor.rut = request.POST.get("txtRut")

        try:
            vendedor.save()
            mensaje = "Vendedor modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al vendedor"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_vendedor.html',data)

def modificarVenta(request, id):

    venta = Venta.objects.get(id=id)

    data = {
        "venta" : venta
    }
    
    # modificar
    if request.POST:
        venta.pedido = request.POST.get("selectPedido") 
        try:
            venta.save()
            mensaje = "Venta modificada"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar la venta"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_venta.html',data)

def modificarCliente(request, id):

    cliente = Cliente.objects.get(id=id)

    data = {
        "cliente" : cliente
    }

    # modificar
    if request.POST:
        cliente.p_nombre = request.POST.get("nombreCli")
        cliente.a_paterno = request.POST.get("apellidoCli")
        cliente.num_contact = request.POST.get("inputTelefono")
        cliente.rut = request.POST.get("rutCli")

        try:
            cliente.save()
            mensaje = "Cliente modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al Cliente"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_clientes.html',data)

def modificarProducto(request, id):

    producto = Producto.objects.get(id=id)

    data = {
        "producto" : producto
    }

    # modificar
    if request.POST:
        producto.nombre = request.POST.get("prodNombre")
        producto.precio = request.POST.get("precioProd")
        producto.img = request.FILES.get("txtImagen")
        producto.desc = request.POST.get("descProd")
        producto.tip_producto = request.POST.get("tipoProd")

        try:
            producto.save()
            mensaje = "Producto modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al Producto"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_producto.html',data)

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
        producto.img = request.FILES.get("txtImagen")
        producto.desc = request.POST.get("descProd")
        producto.tip_producto = request.POST.get("tipoProd")
        try:
            producto.save()
            mensaje = "Producto agregado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo agregar el Producto"
            messages.error(request, mensaje)
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
            messages.error(request, mensaje)

    return render(request, 'core/agregar_vendedor.html')

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
            messages.error(request, mensaje)
    return render(request, 'core/agregar_medioPago.html')

def modificarVendedor(request, id):

    vendedor = Vendedor.objects.get(id=id)

    data = {
        "vendedor": vendedor
    }

    # modificar
    if request.POST:
        vendedor.p_nombre = request.POST.get("primNombre")
        vendedor.s_nombre = request.POST.get("segNombre")
        vendedor.a_paterno = request.POST.get("apPaterno")
        vendedor.a_materno = request.POST.get("apMaterno")
        vendedor.rut = request.POST.get("txtRut")

        try:
            vendedor.save()
            mensaje = "Vendedor modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al vendedor"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_vendedor.html', data)

def modificarVenta(request, id):

    venta = Venta.objects.get(id=id)

    data = {
        "venta": venta
    }

    # modificar
    if request.POST:
        venta.pedido = request.POST.get("selectPedido")
        try:
            venta.save()
            mensaje = "Venta modificada"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar la venta"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_venta.html', data)

def modificarCliente(request, id):

    cliente = Cliente.objects.get(id=id)

    data = {
        "cliente": cliente
    }

    # modificar
    if request.POST:
        cliente.p_nombre = request.POST.get("nombreCli")
        cliente.a_paterno = request.POST.get("apellidoCli")
        cliente.num_contact = request.POST.get("inputTelefono")
        cliente.rut = request.POST.get("rutCli")

        try:
            cliente.save()
            mensaje = "Cliente modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al Cliente"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_clientes.html', data)

def modificarDelivery(request, id):

    delivery = Delivery.objects.get(id=id)

    data = {
        "delivery": delivery
    }

    # modificar
    if request.POST:
        delivery.direccion = request.POST.get("direccionDelivery")
        delivery.telefono = request.POST.get("telefonoDelivery")
        delivery.valor = request.POST.get("valorDelivery")

        try:
            delivery.save()
            mensaje = "Delivery modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar el Delivery"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_delivery.html', data)

def modificarProducto(request, id):

    producto = Producto.objects.get(id=id)

    data = {
        "producto": producto
    }

    # modificar
    if request.POST:
        producto.nombre = request.POST.get("prodNombre")
        producto.precio = request.POST.get("precioProd")
        producto.img = request.POST.get("txtImagen")
        producto.desc = request.POST.get("descProd")
        producto.tip_producto = request.POST.get("tipoProd")

        try:
            producto.save()
            mensaje = "Producto modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar al Producto"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_producto.html', data)

def modificarmedioPago(request, id):

    medioPago = Medio_pago.objects.get(id=id)

    data = {
        "medioPago": medioPago
    }

    # modificar
    if request.POST:
        medioPago.tipo_pago = request.POST.get("medioPago")
        try:
            medioPago.save()
            mensaje = "Medio de Pago modificado"
            messages.success(request, mensaje)
        except:
            mensaje = "No se pudo modificar el Medio de Pago"
            messages.error(request, mensaje)

    return render(request, 'core/modificar_medioPago.html', data)

def eliminarCli(request, id):
    cliente = Cliente.objects.get(id=id)

    try:
        cliente.delete()
        mensaje = "Cliente eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar al Cliente"
        messages.error(request, mensaje)

    return redirect('ver_clientes')

def eliminarVen(request, id):
    vendedor = Vendedor.objects.get(id=id)

    try:
        vendedor.delete()
        mensaje = "Vendedor eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar al Vendedor"
        messages.error(request, mensaje)

    return redirect('ver_vendedores')

def eliminarProd(request, id):
    producto = Producto.objects.get(id=id)

    try:
        producto.delete()
        mensaje = "Producto eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar el Producto"
        messages.error(request, mensaje)

    return redirect('ver_productos')

def eliminarVenta(request, id):
    venta = Venta.objects.get(id=id)

    try:
        venta.delete()
        mensaje = "Venta eliminada"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar la Venta"
        messages.error(request, mensaje)

    return redirect('ventas')

def eliminarMedioPago(request, id):
    medioPago = Medio_pago.objects.get(id=id)

    try:
        medioPago.delete()
        mensaje = "Medio de Pago eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar medio de pago"
        messages.error(request, mensaje)

    return redirect('ver_medios_pago')

def eliminarMiDelivery(request, id):
    miDelivery = Delivery.objects.get(id=id)

    try:
        miDelivery.delete()
        mensaje = "Delivery eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar Delivery"
        messages.error(request, mensaje)

    return redirect('pago')
