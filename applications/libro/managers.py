import datetime

from django.contrib.postgres.search import TrigramSimilarity 
from django.db import models
from django.db.models import (
    Q,
    Count
)    

#__range  para buscar un rango de fechas
class ManagerLibro(models.Manager):
    def buscar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword, 
            fecha__range=('2000-01-01','2010-01-01')
        )
        return resultado

    def buscar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,     
            )
            print(resultado)
            print(kword)
            return resultado
        else:
            resultado = self.all()[:10]
            return resultado


    def buscar_libros2(self, kword, f1, f2):
        d1 = datetime.datetime.strptime(f1, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(f2, "%Y-%m-%d").date()
        resultado = self.filter(
            titulo__icontains=kword, 
            fecha__range=(d1,d2)
        )
        return resultado

    def listar_libros_categoria(self, categoria): 
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
    
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        #parametro add de django sirve para agregar a un libro un autor
        libro.autores.add(autor)
        return libro
        #nota al pie: en lugar de add podemos usar remove para eliminar

    #calcular el numero de prestamos de todos los libro con un Aggregate
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos  = Count('libro_prestamo')
        )
        #devuelve un diccionario con el valor de la operacion aritmetica
        return resultado



class CategoriaLibro(models.Manager):
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()   #para evitar que una consulta devuelva valores repetidos usamos distinc

    
    #nos solicintan el numero de lobros por categoria
    #annotate es la funcion que nos ayuda a resolver eso
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros= Count('categoria_libro')
        )
        for r in resultado:
            print("********")
            print(r, r.num_libros)
        #devuelve un qeryset mas operacion aritmetica
        return resultado