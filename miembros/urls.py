from django.urls import path
from miembros import views
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('registro/', views.register, name='registro'),
    path('perfil/', UserEditView.as_view(), name='perfil'),
    path('<int:pk>/editarperfil/', UserEditPerfilView.as_view(), name='editarperfil'),
    path('crearperfil/', UserCrearPerfilView.as_view(), name='crearperfil'),
    path('password/', CambioPassword.as_view(template_name='miembros/cambio-password.html')),
    path('password-exitosa/', views.password_exitosa, name='password-exitosa'),
    path('logout/', LogoutView.as_view(template_name='miembros/logout.html') , name='logout')
]
