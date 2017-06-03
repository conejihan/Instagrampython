from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^crear_usuario$', views.crear_usuario, name = 'crear_usuario'),
    url(r'^Inicio/$',views.Inicio, name = 'Inicio'),
    url(r'^Perfil/$',views.Perfil, name= 'Perfil'),
    url(r'^Subir/$', views.Subir, name= 'Subir'),
    
    url(r'^Login/$', auth_views.LoginView.as_view(template_name='Login.html', redirect_authenticated_user=True), name= 'Login'),
    url(r'^Logout/$', auth_views.LogoutView.as_view(template_name='Registro.html'), name= 'Logout'),

]
