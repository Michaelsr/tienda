from django import forms
from apps.producto.models import Producto


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'Nombre',
            'PrecioVenta',
            'PrecioVentaCaja',
            'Detalle',


        ]

        labels = {
            'Nombre':'Producto',
            'PrecioVenta':'Precio venta Unidad',
            'PrecioVentaCaja':'Precio venta caja',
            'Detalle':'Detalle',

        }

        widgets = {
            'Nombre': forms.Select(attrs={'class': 'form-control'}),
            'PrecioVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'PrecioVentaCaja': forms.TextInput(attrs={'class': 'form-control'}),
            'Detalle': forms.TextInput(attrs={'class': 'form-control'}),

        }