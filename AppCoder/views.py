from django.shortcuts import render
from .forms import ComentarioForm, PosteoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

def aboutme (request):
    return render (request, "AppCoder/aboutme.html")


class PosteoView (ListView):
    model=Posteo
    template_name="AppCoder/inicio.html"

class PosteoDetalleView (DetailView):
    model=Posteo
    template_name="AppCoder/posteo-detalle.html"


class AddPosteoView (CreateView):
    model=Posteo
    form_class=PosteoForm
    template_name="AppCoder/add-posteo.html"

class UpdatePosteoView (UpdateView):
    model=Posteo
    template_name="AppCoder/update-posteo.html"
    fields=['titulo', 'subtitulo','imagen','cuerpo', ]

class DeletePosteoView (DeleteView):
    model=Posteo
    template_name="AppCoder/delete-posteo.html"
    success_url=reverse_lazy('inicio')

class AddComentarioView (CreateView):
    model=Comentario
    form_class=ComentarioForm
    template_name="AppCoder/add-comentarios.html"
    success_url=reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.posteo_id=self.kwargs['pk'] 
        return super().form_valid(form)

