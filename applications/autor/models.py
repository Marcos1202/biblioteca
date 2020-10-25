from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    nacionalidad = models.CharField("Nacionalidad", max_length=30)
    edad = models.PositiveIntegerField("Edad")

    def __str__(self):
        return self.nombre + '-' + self.apellido
    