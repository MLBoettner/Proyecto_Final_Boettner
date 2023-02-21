from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm, ComentarioForm, PosteoForm
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

def inicio (request):
    return render (request, "AppCoder/inicio.html")

def contact (request):
    return render (request, "AppCoder/contact.html")

def aboutme (request):
    return render (request, "AppCoder/aboutme.html")

def login_request(request):
    form=AuthenticationForm()

    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html')
            else:
                 return render(request, 'AppCoder/login.html', {'mensaje':'Error, datos incorrectos', 'form': form})

        else:
            return render(request, 'AppCoder/login.html', {'mensaje':'Error, datos incorrectos', 'form': form})
    
    return render(request, 'AppCoder/login.html', {'form':form})   

def register(request):
    if request.method== 'POST':

        form=MyUserCreationForm (request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html", {"mensaje":"Usuario Creado :)"})
        
    else:
        form=MyUserCreationForm ()
    
    return render (request, 'AppCoder/registro.html', {"form": form })

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
    success_url=reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.posteo_id=self.kwargs['pk'] 
        return super().form_valid(form)


class AddComentarioView (CreateView):
    model=Comentario
    form_class=ComentarioForm
    template_name="AppCoder/add-comentarios.html"
    success_url=reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.posteo_id=self.kwargs['pk'] 
        return super().form_valid(form)

