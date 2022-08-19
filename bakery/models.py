from django.db import models
from random import randint
# Create your models here.

class Bakeries(models.Model):
    rand = randint(0, 2000)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField(default= rand)
    price = models.FloatField()
    stock = models.IntegerField(default= 0)

       
    def __str__(self):
        return self.name, self.description