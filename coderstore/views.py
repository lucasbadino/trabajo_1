from django.shortcuts import render, redirect
from meat.models import Products
from drink.models import Drinks
from bakery.models import Bakeries

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
   return render(request, 'search_product.html', context = context)

def index(request):
   return render(request,'home_page.html'  )
   
def all_products(request):
   meat = Products.objects.all()
   drink = Drinks .objects.all()
   bakery= Bakeries.objects.all()
   dic = meat.union(drink, bakery)
   context = {	
       'all': dic
                     }
   return render(request, 'all_products.html', context = context)

