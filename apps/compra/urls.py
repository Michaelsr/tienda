from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.compra.views import index
from apps.compra.views import compra_view, compra_list, compra_edit, compra_delete, \
    compraList,compraCreate,compraUpdate, compraDelete


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$',login_required(compraCreate.as_view()) , name='compra_crear'),
	url(r'^listar$',login_required(compraList.as_view()) , name='compra_listar'),
	url(r'^editar/(?P<pk>\d+)/$',login_required(compraUpdate.as_view()) , name='compra_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(compraDelete.as_view()) , name='compra_eliminar'),

]