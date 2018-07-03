from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.producto.views import index
from apps.producto.views import producto_view, producto_list, producto_edit, producto_delete, \
    productoList,productoCreate,productoUpdate, productoDelete


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$',login_required(productoCreate.as_view()) , name='producto_crear'),
	url(r'^listar$',login_required(productoList.as_view()) , name='producto_listar'),
	url(r'^editar/(?P<pk>\d+)/$',login_required(productoUpdate.as_view()) , name='producto_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(productoDelete.as_view()) , name='producto_eliminar'),


]