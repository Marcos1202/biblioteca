from django.shortcuts import render
from django.views.generic import ( 
                                    ListView, 
                                    DetailView
                                )

#models local
from .models import Libro


class  ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/libros.html"

    def get_queryset(self):
        palabraclave = self.request.GET.get("kword", "",)
        #recibiendo fechas
        fecha1 = self.request.GET.get("fecha1", "",)
        fecha2 = self.request.GET.get("fecha2", "",)
        if fecha1 and fecha2:
            return Libro.objects.buscar_libros2(palabraclave, fecha1, fecha2)
        else:
            return Libro.objects.buscar_libros(palabraclave)


class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/libros.html"

    def get_queryset(self):
        palabraclave = self.request.GET.get("kword",'')
                
        return Libro.objects.buscar_libros_trg(palabraclave)


class  ListLibrosCategoria(ListView):
    context_object_name = 'lista_libros_categoria'
    template_name = "libro/libros_categoria.html"

    def get_queryset(self):
        palabraclave = self.request.GET.get("kword", "",)
        if palabraclave:
            return Libro.objects.listar_libros_categoria(palabraclave)
        else:
            return Libro.objects.all()




class LibroDetailView(DetailView):
    
    model = Libro
    template_name = "libro/detalle.html"
