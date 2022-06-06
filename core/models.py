from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Cliente (models.Model):
    p_nombre = models.CharField(max_length=30)
    a_paterno = models.CharField(max_length=20)
    num_contac = models.IntegerField()
    rut = models.CharField(max_length=20)


class Vendedor (models.Model):
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20)
    a_paterno = models.CharField(max_length=20)
    a_materno = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Vendedores"


class Producto (models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    img = models.ImageField(upload_to="productos")
    desc = models.CharField(max_length=200)
    tip_producto = models.CharField(max_length=1)


class Carrito (models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)



class Medio_pago (models.Model):
    tipo_pago = models.CharField(max_length=20)

class Delivery (models.Model):
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    valor = models.IntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    

class Venta (models.Model):
    #--<date=models.CharField(max_length=30) SE ARREGLA MÑA>--#
    subtotal = models.IntegerField()
    total = models.IntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor_id = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True)
    carrito_id = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    pedido = models.CharField(max_length=30)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pago_id = models.ForeignKey(Medio_pago, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True)
