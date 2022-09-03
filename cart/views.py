from django.shortcuts import render, redirect
from cart.cart import Cart
from product.models import Products
from django.contrib.auth.decorators import login_required


def add_product(request,product_id):
    cart=Cart(request)
    product=Products.objects.get(id=product_id)
    cart.add(product)
    return redirect ("cart")
  
  
def delete_product(request, product_id):
    cart = Cart(request)
    product=Products.objects.get(id=product_id)
    cart.delete(product)
    return redirect("cart")


def subtract_product(request, product_id):
    cart = Cart(request)
    product=Products.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("cart")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


def cart(request):
    return render(request, "cart/cart.html")

@login_required
def checkout(request):
    total = 0
    if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                total += int(value["amount"])
                context = {
                    'product' : total
                }
    return render(request, "cart/checkout.html" , context=context)


