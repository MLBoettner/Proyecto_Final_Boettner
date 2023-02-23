from django.urls import path
from miembros import views
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='miembros/logout.html') , name='logout')
]
