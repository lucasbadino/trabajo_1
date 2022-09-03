from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    price= models.FloatField()
    stock = models.IntegerField(default= 0)
    image = models.ImageField(upload_to= 'products_image', blank=True, null=True)
   
    
    
    Carne = 1
    Panaderia = 2
    Bebida = 3
    product_category =[ 
        [Carne, 'Carne'],
        [Panaderia, 'Panaderia'],
        [Bebida, 'Bebida']
     ]
    
    category = models.IntegerField(null=False, blank=False, choices = product_category, default = 1)
    
  
         
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
   
    
        
