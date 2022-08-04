from django.db import models


class Productos(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField()
    price = models.FloatField()
    # def __str__(self):
    #     return self.name
    #     return self.description

class Bebidas(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField()
    price = models.FloatField()

class Panes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    sku = models.IntegerField()
    price = models.FloatField()

