from django.db import models

# Create your models here.

class Proveedor(models.Model):
    NombreProveedor = models.CharField(max_length=35)
    Ruc = models.CharField(max_length=11)
    Direccion = models.CharField(max_length=35)
    Telefono = models.CharField(max_length=9)
    DatosEncargado = models.CharField(max_length=35)
    TelefonoEncargado = models.CharField(max_length=9)
    FechaRegistro = models.DateField()



    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.NombreProveedor, self.Telefono, self.Direccion)

    def __str__(self):
        return self.NombreCompleto()