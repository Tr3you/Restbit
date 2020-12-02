from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.CharField(max_length=3)
    numero_identidad = models.CharField(max_length=15, unique=True)
    numero_celular = models.CharField(max_length=12)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.CharField(max_length=3)
    numero_identidad = models.CharField(max_length=15,unique=True)
    cargo = models.CharField(max_length=100)

class ItemMenu(models.Model):
    codigo_item = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    valor = models.IntegerField()

class Reservacion(models.Model):
    numero_personas = models.IntegerField()
    estado_reservacion = models.CharField(max_length=50, null=True)
    codigo_reserva = models.CharField(max_length=4)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_identidad_cliente = models.ForeignKey(Cliente, to_field='numero_identidad', on_delete=models.CASCADE)

class Comprobante(models.Model):
    estado = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=100)
    total_cuenta = models.IntegerField()
    numero_identidad_cliente = models.ForeignKey(Cliente, to_field='numero_identidad', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

class Pedido(models.Model):
    estado_pedido = models.CharField(max_length=50, null=True)
    numero_pedido = models.CharField(max_length=7)
    codigo_item = models.ForeignKey(ItemMenu, to_field='codigo_item', on_delete=models.CASCADE)
    valor = models.IntegerField()





