from django.db import models

# Create your models here.

class Trabajador (models.Model):

    Nombre = models.CharField(max_length=25)
    ApellidoPaterno = models.CharField(max_length=25)
    ApellidoMaterno = models.CharField(max_length=25)
    Correo = models.CharField(max_length=40)
    DNI = models.CharField(max_length=8)
    Telefono = models.CharField(max_length=9)
    Cargo = models.CharField(max_length=25)
    FechaIngreso = models.DateField()
    Foto = models.ImageField(upload_to='Photo')

    def NombreTrabajador(self):
        cadena = "{0}, {1}, {2}, ({3})"
        return  cadena.format(self.Nombre, self.ApellidoPaterno, self.Telefono, self.Cargo)

    def __str__(self):
        return self.NombreTrabajador()