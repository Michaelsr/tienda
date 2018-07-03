from django.db import models
from apps.compra.models import Compra

# Create your models here.

class Producto(models.Model):
    Nombre = models.ForeignKey(Compra, null=False, blank=False, on_delete=models.CASCADE)
    PrecioVenta = models.DecimalField(max_digits=6, decimal_places=2)
    PrecioVentaCaja = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Detalle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):

        return "{0} {1}".format(self.Nombre, self.PrecioVenta)