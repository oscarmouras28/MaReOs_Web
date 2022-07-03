from django.urls import path
from .views import eliminarVenta, home,boleta,catalogo,pago,registro,recuperar_contrasena,registro_cliente,registro_vendedor,ventas,carrito,ver_vendedores,ver_clientes, ver_productos, eliminarCli, eliminarVen, eliminarProd, ver_pagos, eliminarMedioPago,eliminarMiDelivery, agregar_vendedor, agregarProducto, agregarmedioPago,modificarVendedor,modificarCliente, modificarProducto, modificarVenta, modificarDelivery, modificarmedioPago

urlpatterns = [
    # Home
    path('', home),
    path('home/', home, name= "home"),
    # Boleta
    path('boleta/', boleta, name= "boleta"),
    # Catalogo
    path('catalogo/', catalogo, name= "catalogo"),
    # Pago (api)
    path('pago/', pago, name= "pago"),
    # Actualizar contraseña https://www.youtube.com/watch?v=sFPcd6myZrY mejorar posterior mente
    path('recuperar/', recuperar_contrasena, name= "recuperar"),
    # Registro dividido en 2 Cliente|Vendedor
    path('registro/', registro, name="registro"),
    path('registro_clientes/', registro_cliente, name="registro_clientes"),
    # Deberiamos dejar solo el vendedor registre vendedores, en cambio, de que se registre asi mismo  
    path('registrovendedor/', registro_vendedor, name="registrovendedor"),
    path('agregarVendedor/', agregar_vendedor, name="agregarVendedor"),
    # Ventas
    path('ventas/', ventas, name="ventas"),      
    # Debe ser antes del pago y verse el conteo fuera de el
    path('carrito/', carrito, name="carrito"),
    # Visualizacion de datos (vendedor)
    path('ver_vendedores/', ver_vendedores, name="ver_vendedores"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
    path('ver_productos/', ver_productos, name="ver_productos"),
    path('ver_medios_pago/', ver_pagos, name="ver_medios_pago"),

    # Acciones de vendedor
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('agregarmedioPago/', agregarmedioPago, name="agregarmedioPago"),
    path('eliminarCli/<id>/', eliminarCli, name="eliminarCli"),
    path('eliminarVen/<id>/', eliminarVen, name="eliminarVen"),
    path('eliminarProd/<id>/', eliminarProd, name="eliminarProd"),
    path('eliminarVenta/<id>/', eliminarVenta, name="eliminarVenta"),
    path('eliminarMedioPago/<id>/', eliminarMedioPago, name="eliminarMedioPago"),
    path('eliminarMiDelivery/<id>/', eliminarMiDelivery, name="eliminarMiDelivery"),
    path('modificarVendedor/<id>/', modificarVendedor, name="modificarVendedor"),
    path('modificarCliente/<id>/', modificarCliente, name="modificarCliente"),
    path('modificarProducto/<id>/', modificarProducto, name="modificarProducto"),
    path('modificarVenta/<id>/', modificarVenta, name="modificarVenta"),
    path('modificarDelivery/<id>/', modificarDelivery, name="modificarDelivery"),
    path('modificarmedioPago/<id>/', modificarmedioPago, name="modificarmedioPago"),    
]