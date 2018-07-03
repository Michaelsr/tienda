from django import forms
from apps.compra.models import Compra

class compraForm(forms.ModelForm):
    class Meta:
        model = Compra

        fields = [
            'NombreProducto',
            'PrecioCompra',
            'Proveedor',
            'Categoria',
            'Fecha',
            'CajaPaquete',
            'Detalle',
        ]

        labels = {
            'NombreProducto':'Nombre Producto',
            'PrecioCompra':'Precio Compra',
            'Proveedor':'Proveedor',
            'Categoria':'Categoria',
            'Fecha':'Fecha',
            'CajaPaquete':'Caja Paquete',
            'Detalle':'Detalles',
        }

        widgets = {
            'NombreProducto':forms.TextInput(attrs={'class': 'form-control'}),
            'PrecioCompra':forms.TextInput(attrs={'class': 'form-control'}),
            'Proveedor':forms.Select(attrs={'class': 'form-control'}),
            'Categoria':forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha':forms.DateInput(attrs={'class': 'form-control'}),
            'CajaPaquete':forms.TextInput(attrs={'class': 'form-control'}),
            'Detalle':forms.TextInput(attrs={'class': 'form-control'}),
        }