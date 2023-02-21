from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posteo (models.Model):

    titulo=models.CharField(max_length=255)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo= models.TextField() 
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '|' + str(self.autor)


class Comentario (models.Model):
    posteo=models.ForeignKey(Posteo, related_name="comentarios", on_delete=models.CASCADE)
    nombre=models.CharField(max_length=255)
    cuerpo= models.TextField() 
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.posteo.titulo, self.nombre)
    
    def get_absolute_url(self):
        return reverse ('inicio')