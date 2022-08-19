from django.urls import path
from bakery.views import *



urlpatterns = [
    path('bakeries/', list_bakeries, name= 'bakeries'),
    path('create-bakeries/', form_bakeries, name = 'create-bakeries'),
    path('edit-bakeries/<int:pk>/', edit_bakeries, name='edit-bakeries'),
    path('delete-bakeries/<int:pk>/', delete_bakeries, name='delete-bakeries'),
]
