from django.db import models

#Managers
from .managers import AutorManager

class Persona(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    nacionalidad = models.CharField("Nacionalidad", max_length=30)
    edad = models.PositiveIntegerField("Edad")

    def __str__(self):
        return self.nombre + '-' + self.apellido

    class Meta:
        abstract = True

class Autor(Persona):
    seudonimo = models.CharField(
        "Seudónimo", 
        max_length=50, 
        blank=True
        )

    #viene del managers y se va a las views
    objects = AutorManager()


    