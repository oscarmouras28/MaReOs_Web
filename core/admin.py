from django.contrib import admin
from .models import Cliente,Vendedor,Carrito,Venta,Producto,Delivery,Medio_pago



#Mostrar mas informacion sobre las clases  
class detallecarrito(admin.ModelAdmin):
    search_fields = ["producto_id"]


class detallecliente(admin.ModelAdmin):
    search_fields = ["p_nombre"]


# Register your models here.

admin.site.register(Cliente, detallecliente)
admin.site.register(Vendedor)
admin.site.register(Carrito, detallecarrito)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Delivery)
admin.site.register(Medio_pago)