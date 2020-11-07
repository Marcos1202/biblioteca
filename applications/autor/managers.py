from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado

    def buscar_autor2(self, kword):
        #creando un or
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):
        #exclucion exclucle una edad supoerior a 35
        #en lugar de exclude podemos hacer otro filter esto nos da un filtro dentro de otro filtro
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad__icontains=35) | Q(edad__icontains=25)
        )
        return resultado

    #Mayor que usamos __gt
    #aperson equivale a ,
    #menor que __lt
    def buscar_autor4(self):
        resultado = self.filter(
            edad__gt=30,
            edad__lt=40
        ).order_by('apellido')
        return resultado