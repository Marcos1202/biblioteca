from django.shortcuts import render
from django.views.generic import ListView

#models local
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    
    context_object_name = 'lista_autores'
    template_name = "autor/autores.html"

    def get_queryset(self):
        palabraclave = self.request.GET.get("kword", "",)
        return Autor.objects.buscar_autor2(palabraclave)
    
