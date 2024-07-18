# Create your models here.
# gestion/models.py

from django.db import models

class Veterinaria(models.Model):
    nombre = models.CharField(max_length=100)
    RUC = models.CharField(max_length=13)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class DoctorVeterinario(models.Model):
    nombre_doctor = models.CharField(max_length=100)
    apellido_doctor = models.CharField(max_length=100)
    tiempo_experiencia = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_doctor} {self.apellido_doctor}'
