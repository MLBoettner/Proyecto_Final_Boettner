from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm

# Create your views here.

def inicio (request):
    return render (request, "AppCoder/inicio.html")

def plantas (request):
    return render (request, "AppCoder/plantas.html")

def blog (request):
    return render (request, "AppCoder/blog.html")

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