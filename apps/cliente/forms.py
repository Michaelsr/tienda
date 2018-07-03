from django import forms
from apps.cliente.models import Cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'Nombre',
            'Apellidos',
            'DNI',
            'Sexo',
        ]

        labels = {
            'Nombre':'Nombres',
            'Apellidos':'Apellidos',
            'DNI':'DNI',
            'Sexo':'Sexo',
        }

        widgets = {
            'Nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class': 'form-control'}),
            'DNI':forms.TextInput(attrs={'class': 'form-control'}),
            'Sexo':forms.TextInput(attrs={'class': 'form-control'}),
        }