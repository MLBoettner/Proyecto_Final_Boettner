from django import forms
from .models import *

class PosteoForm(forms.ModelForm):
    class Meta:
        model=Posteo
        fields=('titulo','autor','cuerpo')

        widgets={
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=('nombre','cuerpo')

        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }
