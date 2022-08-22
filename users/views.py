from django.shortcuts import render, redirect
from users.forms import User_registracion_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from coderstore.views import Products,Drinks,Bakeries


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



