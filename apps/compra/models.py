from django.db import models
from apps.proveedor.models import Proveedor
# Create your models here.

class Compra (models.Model):
    NombreProducto = models.CharField(max_length=50)
    PrecioCompra = models.DecimalField(max_digits=6, decimal_places=2)
    Proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)
    Categoria = models.CharField(max_length=50)
    Fecha = models.DateField()
    CajaPaquete = models.DecimalField(max_digits=6, decimal_places=2)
    Detalle = models.CharField(max_length=100, null=True, blank=True)

    def Compra(self):
        cadena = "{0}"
        return  cadena.format(self.NombreProducto)

    def __str__(self):
        return self.Compra()