from django.conf.urls import url
from apps.usuario.views import registroUsuario

urlpatterns = [
	url(r'^registrar', registroUsuario.as_view(), name="registrar")

]