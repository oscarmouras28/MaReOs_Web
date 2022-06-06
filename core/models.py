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
    def __str__(self):
        return self.p_nombre + " " + self.a_paterno 

    class Meta:
        verbose_name_plural = "Cliente"


class Vendedor (models.Model):
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20)
    a_paterno = models.CharField(max_length=20)
    a_materno = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)
    def __str__(self):
        return self.p_nombre + " " + self.a_paterno 
    class Meta:
        verbose_name_plural = "Vendedores"
    def __str__(self):
        return self.p_nombre + " " + self.a_paterno

class Producto (models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    img = models.ImageField(upload_to="productos")
    desc = models.CharField(max_length=200)
    tip_producto = models.CharField(max_length=1)
    class Meta:
        verbose_name_plural = "Producto"
    def __str__(self):
        return self.nombre + " " + self.desc
class Carrito (models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Carrito"
    def __str__(self):
        return self.producto_id.nombre
class Medio_pago (models.Model):
    tipo_pago = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Medio de pago"
    def __str__(self):
        return self.tipo_pago 
class Delivery (models.Model):
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    valor = models.IntegerField()
    class Meta:
        verbose_name_plural = "Delivery"
    def __str__(self):
        return self.direccion 
class Venta (models.Model):
    #--<date=models.CharField(max_length=30) SE ARREGLA MÑA>--#
    subtotal = models.IntegerField()
    total = models.IntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor_id = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    carrito_id = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    pedido = models.CharField(max_length=30)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pago_id = models.ForeignKey(Medio_pago, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Venta"
    def __str__(self):
        return  self.cliente_id + " " + self.pedido