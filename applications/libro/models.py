from django.db import models
from applications.autor.models import Autor

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField("Categoria", max_length=50)
    def __str__(self):
        return self.mombre
    
class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField("titulo", max_length=50)
    fecha = models.DateField("Fecha de lanzamiento")
    portada = models.ImageField("imagen del libro", upload_to="portada", height_field=None, width_field=None, max_length=None)
    visitas = models.PositiveIntegerField("numero de visitas")

    def __str__(self):
        return self.titulo
    
