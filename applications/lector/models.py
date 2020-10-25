from django.db import models
#Aplicaciones locales
from applications.libro.models import Libro

# Create your models here.
class Lector(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    nacionalidad = models.CharField("Nacionalidad", max_length=20)
    edad = models.PositiveIntegerField(default=0)

    def __srt__(self):
        return self.nombre

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField("Fecha", blank=True, null=True)
    devuelto = models.BooleanField()    
    
    def __str__(self):
        return self.libro.Titulo
    



