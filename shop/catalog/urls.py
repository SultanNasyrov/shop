from django.urls import path

from .views import IndexView, DetailView


app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),

]