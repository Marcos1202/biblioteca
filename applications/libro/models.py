from django.db import models
from django.db.models.signals import post_save, pre_save 

#para las imagenes
from PIL import Image
from applications.autor.models import Autor
from .managers import *

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField("Categoria", max_length=50)
    objects = CategoriaLibro()

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
    
class Libro(models.Model):
    #para poder acceder desde categoria usamos el related_name=lo que queramos
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='categoria_libro'
        )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField("Titulo", max_length=50)
    fecha = models.DateField("Fecha de lanzamiento")
    portada = models.ImageField("imagen del libro", upload_to="portada", height_field=None, width_field=None, max_length=None)
    visitas = models.PositiveIntegerField("numero de visitas", default=0)
    stock = models.PositiveIntegerField("Libros disponibles", default=0)
    
    objects = ManagerLibro()

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return "{} - {} cantidad: {}".format(self.id, self.titulo, self.stock)
    
    #Funcion para el guardado de una imagen
    #optimizando el tamaño y usando post_signal
def optimiza_image(sender, instance, **kewords):
    #instance define la modelo
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)
post_save.connect(optimiza_image, sender=Libro)

#def vistas(sender, instance, raw, using, **kewords):
    #instance define la modelo
#    print("**********")
#    vista =  instance.visitas + 1
    #vista.save(instance.visitas)
#pre_save.connect(vistas, sender=Libro)