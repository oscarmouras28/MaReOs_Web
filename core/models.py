from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Cliente (models.Model):
    p_nombre = models.CharField(max_length=30)
    a_paterno = models.CharField(max_length=20)
    num_contac = models.IntegerField()
    rut = models.CharField(max_length=20, null=True)


class Vendedor (models.Model):
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20)
    a_paterno = models.CharField(max_length=20)
    a_materno = models.CharField(max_length=20)
    rut = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = "Vendedores"


class Producto (models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    img = models.ImageField(upload_to="productos", null=True)
    desc = models.CharField(max_length=30)
    tip_producto = models.CharField(max_length=30)


class Carrito (models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)


class Venta (models.Model):
    #--<date=models.CharField(max_length=30) SE ARREGLA MÑA>--#
    subtotal = models.IntegerField()
    total = models.IntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor_id = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    carrito_id = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=30)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Delivery (models.Model):
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    venta_id = models.ForeignKey(Venta, on_delete=models.CASCADE)


class Medio_pago (models.Model):
    tipo_pago = models.CharField(max_length=20)
    venta_id = models.ForeignKey(Venta, on_delete=models.CASCADE)
