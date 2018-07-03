from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.producto.forms import productoForm
from apps.producto.models import Producto

# Create your views here.

def index(request):
	return render(request, 'producto/index.html')


def producto_view(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productoIndex:index')
    else:
        form = productoForm()

    return render(request, 'producto/producto_form.html', {'form':form})

def producto_list(request):
    producto = Producto.objects.all()
    contexto = {'productos':producto}
    return render(request, 'producto/producto_list.html', contexto)

def producto_edit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = productoForm(instance=producto)
    else:
        form = productoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productoIndex:producto_listar')
    return render(request, 'producto/producto_form.html', {'form':form})

def producto_delete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('productoIndex:producto_listar')
    return render(request, 'producto/producto_delete.html', {'productos':producto})


class productoList(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'

class productoCreate(CreateView):
    model = Producto
    form_class = productoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('productoIndex:producto_listar')

class productoUpdate(UpdateView):
    model = Producto
    form_class = productoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('productoIndex:producto_listar')

class productoDelete(DeleteView):
    model = Producto
    form_class = productoForm
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('productoIndex:producto_listar')
