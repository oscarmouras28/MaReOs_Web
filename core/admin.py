from django.contrib import admin
from .models import Usuario,Cliente,Vendedor,Carrito,Venta,Producto,Delivery,Medio_pago

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Carrito)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Delivery)
admin.site.register(Medio_pago)