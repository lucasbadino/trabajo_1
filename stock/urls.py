from django.urls import path
from stock.views import stock
urlpatterns = [
    path('stock/', stock, name= 'stock'),
]
