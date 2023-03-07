from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from AppCoder.models import Perfil

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class EditSettingsForm(UserChangeForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model= User
        fields= ('username', 'email')

class CrearPerfilForm(forms.ModelForm):
    class Meta: 
        model=Perfil
        fields=('bio', 'perfil_pic', 'web_url')
        widgets={
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            #'perfil_pic': forms.ImageField(attrs={'class':'form-control'}),
            'web_url': forms.TextInput(attrs={'class':'form-control'}),
            }

class CambioPasswordForm(PasswordChangeForm):

    old_password = forms.CharField(label='Contraseña Actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir la Nueva Contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ('old_password', ' new_password1', 'new_password2')