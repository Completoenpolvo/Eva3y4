from django.db import models

class RawData(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Persona(models.Model):
    nombre_completo = models.CharField(max_length=255)
    edad_nominal = models.IntegerField()

    def __str__(self):
        return self.nombre_completo
