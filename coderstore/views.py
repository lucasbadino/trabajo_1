from multiprocessing import context
from django.shortcuts import render
from meat.models import Products
from drink.models import Drinks
from bakery.models import Bakeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def home_page(request):
    return render(request, "home_page.html", context={})


def search_products(request):
   search = request.GET['search']
   meat = Products.objects.filter(name__icontains = search)
   drink = Drinks .objects.filter(name__icontains = search)
   bakery= Bakeries.objects.filter(name__icontains = search)
   dic = meat.union(drink, bakery)
   context = {	
       'meat': dic
                     }
   return render(request, '/search_product.html', context = context)

def index(request):
   return render(request, 'index.html' )

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                context = {'message': f'Bienvenido {username} a CoderStore!!!!'}
                return render (request , 'index.html', context=context)
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'error': 'Formulario invalido', 'form': form})
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})
