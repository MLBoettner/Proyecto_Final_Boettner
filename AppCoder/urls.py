from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('plantas/', views.plantas, name='plantas'),
    path('blog/', views.blog, name='blog'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('login/', views.login_request, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html') , name='logout')
]
