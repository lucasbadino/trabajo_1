
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class User_registracion_form(UserCreationForm):
    email = forms.EmailField(required= True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name' ,'last_name','username', 'email', 'password1', 'password2')
        help_texts = {k:'' for k in fields}
        
      
class Form_profile(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100 )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=False)
    imagen = forms.ImageField(required=False)
