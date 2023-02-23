from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', PosteoView.as_view() , name='inicio'),
    path('posteo-detalle/<int:pk>', PosteoDetalleView.as_view() , name='posteo-detalle'),
    path('add-posteo/', AddPosteoView.as_view() , name='add-posteo'),
    path('posteo/update-posteo/<int:pk>', UpdatePosteoView.as_view() , name='update-posteo'),
    path('posteo/delete-posteo/<int:pk>', DeletePosteoView.as_view() , name='delete-posteo'),
    path('posteo-detalle/<int:pk>/add-comentarios/', AddComentarioView.as_view() , name='add-comentarios'),
    path('aboutme/', views.aboutme, name='aboutme')
]
