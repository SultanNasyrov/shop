from django.urls import path

from .views import add_item, clear, change_quantity, delete_item


app_name = 'cart'

urlpatterns = [

    # ajax urls
    path('add-item', add_item, name='add_item'),
    path('clear', clear, name='clear'),
    path('change-quantity', change_quantity, name='change-quantity'),
    path('delete-item', delete_item, name='delete-item'),
]