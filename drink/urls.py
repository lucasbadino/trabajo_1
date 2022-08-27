from django.urls import path
from drink.views import drinks, delete_drinks, edit_drinks, create_drinks, list_drinks, Detail_drinks





urlpatterns = [
    path('drinks/', list_drinks, name='drinks'),
    path('create-drinks/', create_drinks, name='create-drinks'),
    path('edit-drinks/<int:pk>/', edit_drinks, name='edit-drinks'),
    path('delete-drinks/<int:pk>/', delete_drinks, name='delete-drinks'),
    path('detail-drinks/<int:pk>/', Detail_drinks.as_view(), name='detail-dricks'),
]
