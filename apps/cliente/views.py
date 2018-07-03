from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cliente.forms import clienteForm
from apps.cliente.models import Cliente
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'cliente/index.html')


def cliente_view(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('clienteIndex:index')
    else:
        form = clienteForm()

    return render(request, 'cliente/cliente_form.html', {'form':form})

def cliente_list(request):
    cliente = Cliente.objects.all()
    contexto = {'clientes':cliente}
    return render(request, 'cliente/cliente_list.html', contexto)

def cliente_edit(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'GET':
        form = clienteForm(instance=cliente)
    else:
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('clienteIndex:cliente_listar')
    return render(request, 'cliente/cliente_form.html', {'form':form})

def cliente_delete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clienteIndex:cliente_listar')
    return render(request, 'cliente/cliente_delete.html', {'clientes':cliente})


class clienteList(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class clienteCreate(CreateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('clienteIndex:cliente_listar')

class clienteUpdate(UpdateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('clienteIndex:cliente_listar')

class clienteDelete(DeleteView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('clienteIndex:cliente_listar')

