from django.urls import path
from .views import eliminarVenta, home,boleta,catalogo,login,pago,recuperar_contrasena,registro,ventas,carrito,ver_vendedores,ver_clientes, ver_productos, eliminarCli, eliminarVen, eliminarProd, ver_pagos, eliminarMedioPago

urlpatterns = [
    path('', home),
    path('home/', home, name= "home"),
    path('boleta/', boleta, name= "boleta"),
    path('catalogo/', catalogo, name= "catalogo"),
    path('login/', login, name= "login"),
    path('pago/', pago, name= "pago"),
    path('recuperar/', recuperar_contrasena, name= "recuperar"),
    path('registro/', registro, name="registro"),
    path('ventas/', ventas, name="ventas"),
    path('carrito/', carrito, name="carrito"),
    path('ver_vendedores/', ver_vendedores, name="ver_vendedores"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
    path('ver_productos/', ver_productos, name="ver_productos"),
    path('ver_medios_pago/', ver_pagos, name="ver_medios_pago"),
    path('eliminarCli/<id>/', eliminarCli, name="eliminarCli"),
    path('eliminarVen/<id>/', eliminarVen, name="eliminarVen"),
    path('eliminarProd/<id>/', eliminarProd, name="eliminarProd"),
    path('eliminarVenta/<id>/', eliminarVenta, name="eliminarVenta"),
    path('eliminarMedioPago/<id>/', eliminarMedioPago, name="eliminarMedioPago"),
]