from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import registroForm

# Create your views here.

class registroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = registroForm
    success_url = reverse_lazy('proveedorIndex:proveedor_listar')
