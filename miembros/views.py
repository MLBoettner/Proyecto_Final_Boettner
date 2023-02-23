from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm
from django.contrib.auth import login, authenticate



# Create your views here.
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

def register(request):
    if request.method== 'POST':

        form=MyUserCreationForm (request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return redirect ("/")
        
    else:
        form=MyUserCreationForm ()
    
    return render (request, 'miembros/registro.html', {"form": form })