from django.conf.urls import url 
from django.contrib.auth.decorators import login_required
from apps.proveedor.views import index
from apps.proveedor.views import proveedor_view, proveedor_list, proveedor_edit, proveedor_delete, \
	proveedorList,proveedorCreate,proveedorUpdate, proveedorDelete





urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$',login_required(proveedorCreate.as_view()) , name='proveedor_crear'),
	url(r'^listar$',login_required(proveedorList.as_view()) , name='proveedor_listar'),
	url(r'^editar/(?P<pk>\d+)/$',login_required(proveedorUpdate.as_view()) , name='proveedor_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(proveedorDelete.as_view()) , name='proveedor_eliminar'),


]