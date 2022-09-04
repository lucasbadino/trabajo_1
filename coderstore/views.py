from django.shortcuts import render
from product.models import Products


def home_page(request):
    return render(request, "home_page.html", context={})


def search_products(request):
   search = request.GET['search']
   all = Products.objects.filter(name__icontains = search)
   context = {	
       'all': all
                     }
   return render(request, 'search_product.html', context = context)

def index(request):
   return render(request,'home_page.html'  )
   
def all_products(request):
   all = Products.objects.all()
   context = {	
       'list': all
                     }
   return render(request, 'all_products.html', context = context)


def about_us(request):
   
   return render(request, 'about.html', context={})
