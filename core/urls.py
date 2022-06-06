from django.urls import path
from .views import home,boleta,catalogo,pago,recuperar_contrasena,registro,ventas,carrito

urlpatterns = [
    path('', home),
    path('home/', home, name= "home"),
    path('boleta/', boleta, name= "boleta"),
    path('catalogo/', catalogo, name= "catalogo"),
    path('pago/', pago, name= "pago"),
    path('recuperar/', recuperar_contrasena, name= "recuperar"),
    path('registro/', registro, name="registro"),
    path('ventas/', ventas, name="ventas"),
    path('carrito/', carrito, name="carrito"),

]
