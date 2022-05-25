from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Usuario (models.Model):
    correo=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)

    cliente_id=models.ForeignKey(Cliente,on_delete=models.CASCADE)
class Cliente (models.Model):
    p_nombre=models.CharField(max_length=30)
    num_contac=models.IntegerField()
    usuario_id=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Vendedor (models.Model):
     p_nombre=models.CharField(max_length=20)
     s_nombre=models.CharField(max_length=20)
     a_paterno=models.CharField(max_length=20)
     a_materno=models.CharField(max_length=20)
     visualidad_pedido=models.CharField(max_length=1)
class Carrito (models.Model):
    lista_prod=models.CharField(max_length=30)

class Venta (models.Model):
    #--<date=models.CharField(max_length=30)>--#   
    subtotal=models.IntegerField() 
    total=models.IntegerField() 
    cliente_id=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    vendedor_id=models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    carrito_id=models.ForeignKey(Carrito,on_delete=models.CASCADE)
    pedido=models.CharField(max_length=30)
class Producto (models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    venta_id=models.ForeignKey(Venta,on_delete=models.CASCADE)

class Delivery (models.Model):
    direccion=models.CharField(max_length=30)
    telefono=models.IntegerField()
    venta_id=models.ForeignKey(Venta,on_delete=models.CASCADE)

class Medio_pago (models.Model):
    debito=models.CharField(max_length=20)
    transferencia=models.CharField(max_length=20)
    flow=models.CharField(max_length=20)
    efectivo=models.CharField(max_length=20)
    venta_id=models.ForeignKey(Venta,on_delete=models.CASCADE)
    


 

