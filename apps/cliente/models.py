from django.db import models

# Create your models here.

class Cliente (models.Model):
    Nombre = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25, null=True, blank=True)
    DNI = models.CharField(max_length=8, null=True)
    Sexo = models.CharField(max_length=10)

    def Cliente(self):
        cadena = "{0}, {1} "
        return cadena.format(self.Nombre, self.DNI)

    def __str__(self):
        return self.Cliente()