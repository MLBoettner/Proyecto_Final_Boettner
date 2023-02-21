from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', PosteoView.as_view() , name='inicio'),
    path('posteo-detalle/<int:pk>', PosteoDetalleView.as_view() , name='posteo-detalle'),
    path('add-posteo/', AddPosteoView.as_view() , name='add-posteo'),
    path('posteo-detalle/<int:pk>/add-comentarios/', AddComentarioView.as_view() , name='add-comentarios'),
    path('contact/', views.contact, name='contact'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('login/', views.login_request, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html') , name='logout')
]
