from datetime import  date

from django.shortcuts import render
from django.views.generic.edit import FormView
#para los errores
from django.http import HttpResponseRedirect

from .models import Prestamo
from .form import PrestamoForm, MultiplePrestamoForm

class RegistrarPrestamo(FormView):
    template_name = 'lector/agregar.html'
    #aqui especificamos un formulario
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        #siempre que interactuemos con la orm de django llamamos al metodo objects
        Prestamo.objects.create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False 
        ) 

        #otra forma de guardar
        """ prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False 
        )
        prestamo.save()
        libro =  form.cleaned_data['libro']
        libro.stock = libro.stock
        libro.save()""" 
        return super(RegistrarPrestamo, self ).form_valid(form)



class addPrestamo(FormView):
    template_name = 'lector/agregar.html'
    #aqui especificamos un formulario
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        #validar que un registro no exista en la base de datos
        #si existe no lo creamos, lo recuperamos
        #si no existe lo creamos

        obj, create = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults={
                'fecha_prestamo' : date.today()
            }

        )

        if create:
            return super(addPrestamo, self ).form_valid(form)
        else:
            return HttpResponseRedirect('/')



class AddMultiplePrestamo(FormView):
    template_name = 'lector/miltiple_prestamo.html'
    #aqui especificamos un formulario
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):
        prestamos= []
        for lib in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = lib,
                fecha_prestamo = date.today(),
                devuelto = False 
            )
            prestamos.append(prestamo)

        #para evitar guardar muchas registros
        #guardamos una lista
        Prestamo.objects.bulk_create(
            prestamos
        )



        return super(AddMultiplePrestamo, self ).form_valid(form)
