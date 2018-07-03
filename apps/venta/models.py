from django.db import models
from apps.cliente.models import Cliente
from apps.producto.models import *
from apps.trabajador.models import *
# Create your models here.

class VentaFactura (models.Model):
    Produc = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    NombreTrabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    Igv = models.DecimalField(max_digits=6, decimal_places=2)
    Total = models.DecimalField(max_digits=6, decimal_places=2)
    FechaVenta = models.DateField()

    def VentaFactura(self):
        cadena = "{0}, {1} {2}"
        return cadena.format(self.Produc.Nombre, self.Total, self.NombreTrabajador.Nombre)

    def __str__(self):
        return self.VentaFactura()