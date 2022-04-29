from django.urls import path
from .views import home,boleta,catalogo,login,pago,recuperar_contrasena,registro,ventas

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
]