from django.db import models

# Create your models here.
class Blog (models.Model):

    titulo=models.CharField(max_length=40)
    descripcion= models.TextField() 
    fecha=models.DateTimeField()

class Planta (models.Model):

    nombre=models.CharField(max_length=40)
    descripcion= models.TextField() 
    fechapublicacion=models.DateTimeField()
