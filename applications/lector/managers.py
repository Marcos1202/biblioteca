import datetime

from django.db import models
from django.db.models.functions import Lower
from django.db.models import (
    Q,
    Count,
    #Avg para calcular promedios
    Avg,
    #para hacer sumas
    Sum
)    



class PrestamoManager(models.Manager):
    def libro_promedio_edades(self):
        resultado = self.filter(
            libro__id=3
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad')
        )
        return resultado

    #Para saber cuantas veces se presta un libro
    def num_libros_prestados(self):
        #necesitamos values para
        #elegir el palametro en base a que agrupar
        #esto hace que nos devuelva un diccionario
        resultado = self.values(
            'libro'
            #aqui agregamos una coma y despues mas comillas
            #de esta forma tenemos una doble agrupacion 
            #o triple o infinita
        ).annotate(
            num_prestamo=Count('libro'),
            #Lower para mejorar la salida del diccionario agregando atributos
            titulo = Lower('libro__titulo')
        )
        for r in resultado:
            print("------")
            #asi es como se imprime un diccionario
            print(r, r['num_prestamo'])
        return resultado


