
from django.shortcuts import render, redirect
from users.forms import Form_profile
from users.forms import User_registracion_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from product.models import Products
from users.models import *
from django.contrib.auth.models import User
import os


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                
                
                login(request, user)
                all = Products.objects.all()
                context = {	
                    'list': all
                     }
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
            return render (request , 'all_products.html', context=context)
                
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'error': 'Formulario invalido', 'form': form})
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def register_request(request):
    if request.method == 'POST':
        form = User_registracion_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors': form.errors}
            form = User_registracion_form
            context ['form'] = form
            return render(request, 'user/register.html', context=context)
  
    elif request.method == 'GET':
        form = User_registracion_form()
        context = {
            'form' : form
        }
        return render(request, 'user/register.html', context= context)

def user_profile(request, pk):

    if request.method == 'POST':
       
        form = Form_profile(request.POST , request.FILES)
        if form.is_valid():
            profile = User.objects.get(id=pk)
            profile2 = User_profile.objects.get()
            profile.first_name = form.cleaned_data['nombre']
            profile.last_name = form.cleaned_data['apellido']
            profile.email = form.cleaned_data['email']
            profile2.address = form.cleaned_data['direccion']
            profile2.phone = form.cleaned_data['telefono']
            profile.password1 = form.cleaned_data['password1']
            profile.password2= form.cleaned_data['password2']
            if len(request.FILES) != 0:
                try:
                    if len(profile2.image) > 0:
                        os.remove(profile2.image.path)
                    profile2.image = request.FILES['imagen']
                    profile2.save()
                except:
                    profile2.image = request.FILES['imagen']
                    profile2.save()
            else:
                profile2.image.delete(profile2.image.path)
            profile2.save()
            profile.save()
            return redirect('confirmation')

    elif request.method == 'GET':
        if request.user.is_authenticated:
       
            profile = User.objects.get(id=pk)
            profile2 = User_profile.objects.get()
            form = Form_profile (initial={
                #'username': profile.username,
                'nombre': profile.first_name,
                'apellido': profile.last_name,
                'email': profile.email,
                'direccion':profile2.address,
                'telefono': profile2.phone,
                'password': profile.password,
                'password': profile.password,
                'imagen':profile2.image })
            context = {'form': form}
            return render(request, 'user/user_profile.html', context=context)
        else:
            return redirect('confirmation')

def confirmation(request):  
    return render(request, 'user/confirmation.html',context={})


def profile_complete(request, pk ):
    profile2 = User.objects.get(id = pk)
    profile = User_profile.objects.get()

    context = {
        'profile': profile
    }
    return render(request, 'user/profile_complete.html' , context=context)