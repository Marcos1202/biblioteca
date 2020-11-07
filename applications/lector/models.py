from django.db import models
from django.db.models.signals import post_delete

#Aplicaciones locales
from applications.libro.models import Libro
from applications.autor.models import Persona


from .managers import *

# Create your models here.
class Lector(Persona):
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    
    )
    fecha_prestamo = models.DateField("Fecha de prestamo", blank=True, null=True)
    fecha_devolucion = models.DateField("Fecha de devolución", blank=True, null=True)
    devuelto = models.BooleanField()    
    objects = PrestamoManager()

    #sobre escribiendo la funcion save de los models
    def save(self, *args, **kwargs):
        print('+++++++++++')
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        return super(Prestamo, self).save( *args, **kwargs)
    def __str__(self):
        return self.libro.titulo + 'fue prestado a: '+ self.lector.nombre
    
def update_libro_stock(sender, instance,  **kwargs):
    #Actualizaar el stok en caso de que se un delete
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save() 

post_delete.connect(update_libro_stock, sender=Prestamo)



