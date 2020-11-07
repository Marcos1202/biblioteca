from django.db import models


# Create your models here.
class Persona(models.Model):

    full_name = models.CharField("Nombres", max_length=50)
    pais = models.CharField("Pais", max_length=50)
    Pasaporte = models.CharField("Pasaporte", max_length=50)
    edad = models.IntegerField("Edad")
    apelativo = models.CharField("Apelativo", max_length=10)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        #para que nuestra tabla tenga el nombre que queremos
        db_table = 'persona'
        unique_together = ['pais', 'apelativo']
        #mietras sean validaciones simples las podemos hacer aqui
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        #gte mayor o igual

        #esta linea evita que exita una tabla persona
        #ya que solo trabajaremos con empleados y clientes
        abstract = True

    def __str__(self):
        return self.full_name

#Hacemos una herencia para registrar clientes y empleados sobre persona
class Empleado(Persona):
    empleo = models.CharField('Empleo', max_length=50)

class Cliente(Persona):
    empleo = models.CharField('Empleo', max_length=50)
