from django.urls import path

from .views import CartIndexView
from .views import add_item, clear, change_quantity, delete_item


app_name = 'cart'

urlpatterns = [
    path('', CartIndexView.as_view(), name='index'),
    # ajax urls
    path('add-item', add_item, name='add_item'),
    path('clear', clear, name='clear'),
    path('change-quantity', change_quantity, name='change-quantity'),
    path('delete-item', delete_item, name='delete-item'),
]