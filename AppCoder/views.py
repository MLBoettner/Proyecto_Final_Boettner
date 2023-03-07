from django.shortcuts import render
from .forms import ComentarioForm, PosteoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

# Vista de la Pagina AboutMe
def aboutme (request):
    return render (request, "AppCoder/aboutme.html")

# Vista de la pagina inicial que muestra la lista de posteo
class PosteoView (ListView):
    model=Posteo
    template_name="AppCoder/inicio.html"

# Vista de la pagina que muestra en detalle un posteo en particular
class PosteoDetalleView (DetailView):
    model=Posteo
    template_name="AppCoder/posteo-detalle.html"

# Vista de la pagina que permite crear un posteo
class AddPosteoView (CreateView):
    model=Posteo
    form_class=PosteoForm
    template_name="AppCoder/add-posteo.html"

# Vista de la pagina que permite modificar un posteo ya creado por el usuario logueado
class UpdatePosteoView (UpdateView):
    model=Posteo
    template_name="AppCoder/update-posteo.html"
    fields=['titulo', 'subtitulo','imagen','cuerpo', ]

# Vista de la pagina que permite eliminar un posteo ya creado por el usuario logueado
class DeletePosteoView (DeleteView):
    model=Posteo
    template_name="AppCoder/delete-posteo.html"
    success_url=reverse_lazy('inicio')

# Vista de la pagina que permite agregar comentarios a los posteos, no es necesario estar logueado
class AddComentarioView (CreateView):
    model=Comentario
    form_class=ComentarioForm
    template_name="AppCoder/add-comentarios.html"
    success_url=reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.posteo_id=self.kwargs['pk'] 
        return super().form_valid(form)

