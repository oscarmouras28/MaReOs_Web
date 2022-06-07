from django.urls import path
<<<<<<< HEAD
from .views import eliminarVenta, home,boleta,catalogo,pago,recuperar_contrasena,registro_cliente,registro_vendedor,ventas,carrito,ver_vendedores,ver_clientes, ver_productos, eliminarCli, eliminarVen, eliminarProd, ver_pagos, eliminarMedioPago,eliminarMiDelivery, agregar_vendedor, agregarProducto, agregarmedioPago,modificarVendedor,modificarCliente, modificarProducto, modificarVenta
=======
from .views import eliminarVenta, home,boleta,catalogo,pago,recuperar_contrasena,registro,ventas,carrito,ver_vendedores,ver_clientes, ver_productos, eliminarCli, eliminarVen, eliminarProd, ver_pagos, eliminarMedioPago,eliminarMiDelivery, agregar_vendedor, agregarProducto, agregarmedioPago,modificarVendedor,modificarCliente, modificarProducto, modificarVenta, modificarDelivery, modificarmedioPago
>>>>>>> 5004a7e7feadcb6ac1ac9b334380051bd4df3f6e

urlpatterns = [
    path('', home),
    path('home/', home, name= "home"),
    path('boleta/', boleta, name= "boleta"),
    path('catalogo/', catalogo, name= "catalogo"),
    path('pago/', pago, name= "pago"),
    path('recuperar/', recuperar_contrasena, name= "recuperar"),
    path('registro/', registro_cliente, name="registro"),
    path('ventas/', ventas, name="ventas"),
    path('carrito/', carrito, name="carrito"),
    path('ver_vendedores/', ver_vendedores, name="ver_vendedores"),
    path('registrovendedor/', registro_vendedor, name="registrovendedor"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
    path('ver_productos/', ver_productos, name="ver_productos"),
    path('ver_medios_pago/', ver_pagos, name="ver_medios_pago"),
    path('eliminarCli/<id>/', eliminarCli, name="eliminarCli"),
    path('eliminarVen/<id>/', eliminarVen, name="eliminarVen"),
    path('eliminarProd/<id>/', eliminarProd, name="eliminarProd"),
    path('eliminarVenta/<id>/', eliminarVenta, name="eliminarVenta"),
    path('eliminarMedioPago/<id>/', eliminarMedioPago, name="eliminarMedioPago"),
    path('eliminarMiDelivery/<id>/', eliminarMiDelivery, name="eliminarMiDelivery"),
    path('agregarVendedor/', agregar_vendedor, name="agregarVendedor"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('agregarmedioPago/', agregarmedioPago, name="agregarmedioPago"),
    path('modificarVendedor/<id>/', modificarVendedor, name="modificarVendedor"),
    path('modificarCliente/<id>/', modificarCliente, name="modificarCliente"),
    path('modificarProducto/<id>/', modificarProducto, name="modificarProducto"),
    path('modificarVenta/<id>/', modificarVenta, name="modificarVenta"),
    path('modificarDelivery/<id>/', modificarDelivery, name="modificarDelivery"),
    path('modificarmedioPago/<id>/', modificarmedioPago, name="modificarmedioPago"),    
]