from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.compra.forms import compraForm
from apps.compra.models import Compra
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'compra/index.html')


def compra_view(request):
    if request.method == 'POST':
        form = compraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('compraIndex:index')
    else:
        form = compraForm()

    return render(request, 'compra/compra_form.html', {'form':form})

def compra_list(request):
    compra = Compra.objects.all()
    contexto = {'compras':compra}
    return render(request, 'compra/compra_list.html', contexto)

def compra_edit(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    if request.method == 'GET':
        form = compraForm(instance=compra)
    else:
        form = compraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
        return redirect('compraIndex:index')
    return render(request, 'compra/compra_form.html', {'form':form})

def compra_delete(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    if request.method == 'POST':
        compra.delete()
        return redirect('compraIndex:compra_listar')
    return render(request, 'compra/compra_delete.html', {'compras':compra})


class compraList(ListView):
    model = Compra
    template_name = 'compra/compra_list.html'

class compraCreate(CreateView):
    model = Compra
    form_class = compraForm
    template_name = 'compra/compra_form.html'
    success_url = reverse_lazy('compraIndex:compra_listar')

class compraUpdate(UpdateView):
    model = Compra
    form_class = compraForm
    template_name = 'compra/compra_form.html'
    success_url = reverse_lazy('compraIndex:compra_listar')

class compraDelete(DeleteView):
    model = Compra
    form_class = compraForm
    template_name = 'compra/compra_delete.html'
    success_url = reverse_lazy('compraIndex:compra_listar')

