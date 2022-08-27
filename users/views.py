
from multiprocessing import context
from django.shortcuts import render, redirect
from users.forms import Form_profile
from users.forms import User_registracion_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from coderstore.views import Products,Drinks,Bakeries
from users.models import *
from django.contrib.auth.models import User


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
                meat = Products.objects.all()
                drink = Drinks .objects.all()
                bakery= Bakeries.objects.all()
                dic = meat.union(drink, bakery)
                context = {	
                    'all': dic
                                    }
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
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.email = form.cleaned_data['email']
            profile2.address = form.cleaned_data['address']
            profile2.phone = form.cleaned_data['phone']
            profile.password1 = form.cleaned_data['password1']
            profile.password2= form.cleaned_data['password2']
            profile2.image =form.cleaned_data['image']
            profile2.save()
            profile.save()

            return redirect('confirmation')

    elif request.method == 'GET':
        if request.user.is_authenticated:
       
            profile = User.objects.get(id=pk)
            profile2 = User_profile.objects.get()
            form = Form_profile (initial={
                #'username': profile.username,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'email': profile.email,
                'address':profile2.address,
                'phone': profile2.phone,
                'password': profile.password,
                'password': profile.password,
                'image':profile2.image })
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