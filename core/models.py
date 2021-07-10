from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre


class Rams(models.Model):
    nombre = models.CharField(max_length=70)
    precio = models.IntegerField()
    capacidad = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    frecuencia = models.CharField(max_length=70)
    formato = models.CharField(max_length=70)
    voltaje = models.CharField(max_length=70)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="Rams", null=True)

    def __str__(self):
        return self.nombre

class Juegos(models.Model):
    nombre =  models.CharField(max_length=70)
    procesador = models.CharField(max_length=70)
    memoria = models.CharField(max_length=70)
    graficos = models.CharField(max_length=80)
    almacenamiento = models.CharField(max_length=70)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    caratula = models.ImageField(upload_to="games", null=True)

    def __str__(self):
        return self.nombre

class Gabinete(models.Model):
    nombre = models.CharField(max_length=70)
    formato = models.CharField(max_length=70)
    fuentePoder = models.CharField(max_length=70)
    ubicacion = models.CharField(max_length=70)
    panel = models.CharField(max_length=70)
    ventiladores = models.CharField(max_length=70)
    precio = models.IntegerField()
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="gabinetes", null=True)

    def __str__(self):
        return self.nombre        

class Procesador(models.Model):
    nombre = models.CharField(max_length=70)
    frecuencia = models.CharField(max_length=70)
    nucleos = models.CharField(max_length=70)
    socket = models.CharField(max_length=70)
    cache = models.CharField(max_length=70)
    arquitectura = models.CharField(max_length=70)
    precio = models.IntegerField()
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="procesadores", null=True)

    def __str__(self):
        return self.nombre

class GPU(models.Model):
    nombre = models.CharField(max_length=70)
    memoria = models.CharField(max_length=70)
    frecuencia = models.CharField(max_length=70)
    marca = models.CharField(max_length=70)
    nucleos = models.CharField(max_length=70)
    precio = models.IntegerField()
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="Graficos", null=True)

    def __str__(self):
        return self.nombre        

