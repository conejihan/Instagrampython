from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^crear_usuario$', views.crear_usuario, name = 'crear_usuario'),
    url(r'^Entrada/$', views.Entrada, name = 'Entrada'),
    url(r'^Inicio/$',views.Inicio, name = 'Incio'),
    url(r'^Perfil/$',views.Perfil, name= 'Perfil'),
]
