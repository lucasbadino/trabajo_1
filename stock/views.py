from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from bakery.models import Bakeries
from drink.models import Drinks

from meat.models import Products

def stock(request):
        meat = Products.objects.all()
        drink = Drinks .objects.all()
        bakery= Bakeries.objects.all()
        dic = meat.union(drink, bakery)
        context = {	
            'all': dic
                            }
        return render(request, 'stock.html', context = context)
    