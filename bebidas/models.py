from django.db import models

# Create your models here.

class Bebidas(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=60)