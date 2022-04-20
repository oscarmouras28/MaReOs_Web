
from django.urls import path
from views import home,catalogo,boleta,login,registro,ventas,recuperarContraseña,pago
urlspatterns=[
    path('',home,name="home")
]  