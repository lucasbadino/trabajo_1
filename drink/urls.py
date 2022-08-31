from django.urls import path
from drink.views import delete_drinks, create_drinks, list_drinks, Detail_drinks,Update_drinks





urlpatterns = [
    path('drinks/', list_drinks, name='drinks'),
    path('create-drinks/', create_drinks, name='create-drinks'),
    path('edit-drinks/<int:pk>/', Update_drinks.as_view(), name='edit-drinks'),
    path('delete-drinks/<int:pk>/', delete_drinks, name='delete-drinks'),
    path('detail-drinks/<int:pk>/', Detail_drinks.as_view(), name='detail-dricks'),
]
