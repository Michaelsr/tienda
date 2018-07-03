from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.proveedor.forms import proveedorForm

from apps.proveedor.models import Proveedor

# Create your views here.

def index(request):
	return render(request, 'proveedor/index.html')


def proveedor_view(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('proveedorIndex:index')
    else:
        form = proveedorForm()

    return render(request, 'proveedor/proveedor_form.html', {'form':form})

def proveedor_list(request):
    proveedor = Proveedor.objects.all()
    contexto = {'proveedores':proveedor}
    return render(request, 'proveedor/proveedor_list.html', contexto)

def proveedor_edit(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == 'GET':
        form = proveedorForm(instance=proveedor)
    else:
        form = proveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
        return redirect('proveedorIndex:proveedor_listar')
    return render(request, 'proveedor/proveedor_form.html', {'form':form})

def proveedor_delete(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedorIndex:proveedor_listar')
    return render(request, 'proveedor/proveedor_delete.html', {'proveedores':proveedor})


class proveedorList(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'

class proveedorCreate(CreateView):
    model = Proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedorIndex:proveedor_listar')

class proveedorUpdate(UpdateView):
    model = Proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedorIndex:proveedor_listar')

class proveedorDelete(DeleteView):
    model = Proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_delete.html'
    success_url = reverse_lazy('proveedorIndex:proveedor_listar')
