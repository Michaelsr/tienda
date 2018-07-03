from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.cliente.views import index
from apps.cliente.views import cliente_view, cliente_list, cliente_edit, cliente_delete, \
    clienteList,clienteCreate,clienteUpdate, clienteDelete


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$',login_required(clienteCreate.as_view()) , name='cliente_crear'),
	url(r'^listar$',login_required(clienteList.as_view()) , name='cliente_listar'),
	url(r'^editar/(?P<pk>\d+)/$',login_required(clienteUpdate.as_view()) , name='cliente_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(clienteDelete.as_view()) , name='cliente_eliminar'),

]