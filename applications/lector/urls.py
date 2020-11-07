from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path(
        'agregar_prestamo/', 
        views.addPrestamo.as_view(), 
        name='prestamo'
    ),
    path(
        'multiple_prestamo/', 
        views.AddMultiplePrestamo.as_view(), 
        name='multiple_prestamo'
    ),
]