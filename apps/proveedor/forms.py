from django import forms
from apps.proveedor.models import Proveedor


class proveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor

		fields = [
			'NombreProveedor',
			'Ruc',
			'Direccion',
			'Telefono',
			'DatosEncargado',
			'TelefonoEncargado',
			'FechaRegistro',

		]

		labels = {
			'NombreProveedor':'Nombre del Probeedor',
			'Ruc':'Ruc',
			'Direccion':'Direccion',
			'Telefono':'Telefono',
			'DatosEncargado':'Nombre Encargado',
			'TelefonoEncargado':'Telefono Encargado',
			'FechaRegistro':'Fecha Registro',

		}	

		widgets = {
			'NombreProveedor':forms.TextInput(attrs={'class':'form-control'}),
			'Ruc': forms.TextInput(attrs={'class':'form-control'}),
			'Direccion': forms.TextInput(attrs={'class':'form-control'}),
			'Telefono': forms.TextInput(attrs={'class':'form-control'}),
			'DatosEncargado': forms.TextInput(attrs={'class':'form-control'}),
			'TelefonoEncargado': forms.TextInput(attrs={'class':'form-control'}),
			'FechaRegistro': forms.TextInput(attrs={'class':'form-control'}),
		}