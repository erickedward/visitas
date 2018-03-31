from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^visita/$', views.visitas_mostrar, name='visitas_mostrar'),
	url(r'^visita/(?P<pag>[0-9]+)/visitas/$', views.visitas_list, name='visitas_paginacion'),
	url(r'^visita/new/$', views.visita_add, name='visita_add'),
	url(r'^visita/(?P<pk>[0-9]+)/editar/$', views.visita_editar, name='visita_editar'),
	url(r'^visita/(?P<pk>[0-9]+)/salida/$', views.visita_salida, name='visita_salida'),
	url(r'^visita/(?P<pk>[0-9]+)/eliminar/$', views.visita_eliminar, name='visita_eliminar'),
	url(r'^departamentos/(?P<pag>[0-9]+)/departamentos/$', views.departamentos, name='departamentos'),
	url(r'^departamentos/nuevo/$', views.departamento_add, name='departamento_add'),
	url(r'^departamentos/(?P<pk>[0-9]+)/eliminar/$', views.departameto_eliminar, name='departameto_eliminar'),
	url(r'^departamentos/(?P<pk>[0-9]+)/editar/$', views.departameto_editar, name='departameto_editar'),
]