from django.urls import path
from .views import home,boleta,catalogo,login,pago,recuperar_contrasena,registro,ventas,carrito,ver_vendedores,ver_clientes, ver_productos

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
]