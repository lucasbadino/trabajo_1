from django.shortcuts import render
from product.models import Products


def stock(request):
        products = Products.objects.all()
        context = {	
            'products': products
                            }
        return render(request, 'stock.html', context = context)
    