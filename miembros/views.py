from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm, CambioPasswordForm, EditSettingsForm, CrearPerfilForm
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from AppCoder.models import Perfil


# Create your views here.

# Vista de la pagina para loguearse al blog 
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
                return redirect ("/")
            else:
                 return render(request, 'miembros/login.html', {'mensaje':'Error, datos incorrectos', 'form': form})

        else:
            return render(request, 'miembros/login.html', {'mensaje':'Error, datos incorrectos', 'form': form})
    
    return render(request, 'miembros/login.html', {'form':form})   

# Vista de la pagina para registrarse y crear un usuario
def register(request):
    if request.method== 'POST':

        form=MyUserCreationForm (request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render (request, 'miembros/registro-exitoso.html')  
    else:
        form=MyUserCreationForm ()
    
    return render (request, 'miembros/registro.html', {"form": form })

# Vista de la pagina que permite modificar los settings de un Perfil
class UserEditView (UpdateView):
    form_class=EditSettingsForm
    template_name='miembros/perfil.html'
    success_url=reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    
# Vista de la pagina que permite modificar el Perfil una vez que el usuario loguedo ya lo creo    
class UserEditPerfilView(UpdateView):
     model=Perfil
     template_name='miembros/editarperfil.html'
     fields=['bio', 'perfil_pic', 'web_url']
     success_url=reverse_lazy('inicio')
    
# Vista de la pagina que permite crear el Perfil  
class UserCrearPerfilView(CreateView):
     model=Perfil
     form_class=CrearPerfilForm
     template_name='miembros/crearperfil.html'
     
     def form_valid(self,form):
         form.instance.user=self.request.user
         return super().form_valid(form)
    
# Vista que permite el cambio de contraseña        
class CambioPassword (PasswordChangeView):
    form_class=CambioPasswordForm
    success_url=reverse_lazy('password-exitosa')


def password_exitosa(request):
    return render (request, 'miembros/password-exitosa.html',{})
