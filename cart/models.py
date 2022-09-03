from django.db import models
from django. contrib.auth.models import User
from bakery.models import Bakeries
from meat.models import Products
from drink.models import Drinks
from itertools import chain

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, blank=True)
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name
    
 
class Product(models.Model):
  product= models.ForeignKey(Drinks,to_field='name', on_delete=models.SET_NULL, blank=True, null=True)
  product1= models.ForeignKey(Products, to_field='name', on_delete=models.SET_NULL, blank=True, null=True)
  product2= models.ForeignKey(Bakeries, to_field='name', on_delete=models.SET_NULL, blank=True, null=True) 
  
class Meta:
    abstract = True
  
def __str__(self):
        return self.name
    
    

  




class Prueba(models.Model):
    todos_productos = models.ForeignKey(Product, on_delete=models.CASCADE)
  
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Products'   

   



