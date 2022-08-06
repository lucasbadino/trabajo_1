from django.shortcuts import render

def panes(request):
    rand = randint(0, 2000)
    al1 = Productos.objects.create(name = 'Carne', description = 'Carne de ternera', sku = rand, price = 2000)
    context = {
        'carne': al1
    }
    return render(request, 'alimentos.html', context=context)


def lista_panes(request):
    
    all = Productos.objects.all() 
     
    context ={
        'lista' : all
    }
    return render(request,'alimentos.html', context = context)

