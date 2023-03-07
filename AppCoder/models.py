from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posteo (models.Model):

    titulo=models.CharField(max_length=255)
    subtitulo=models.CharField(max_length=255)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(null=True, blank=True, upload_to="imagenes/")
    cuerpo=models.TextField() 
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '|' + str(self.autor)

    def get_absolute_url(self):
        return reverse ('inicio')

class Comentario (models.Model):
    posteo=models.ForeignKey(Posteo, related_name="comentarios", on_delete=models.CASCADE)
    nombre=models.CharField(max_length=255)
    cuerpo= models.TextField() 
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.posteo.titulo, self.nombre)
    

class Perfil (models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio=models.TextField() 
    perfil_pic=models.ImageField(null=True, blank=True, upload_to="imagenes/perfil/")
    web_url=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('inicio')