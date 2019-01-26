from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.index.urls')),
    path('catalog', include('shop.catalog.urls', namespace='catalog')),
    path('cart', include('shop.cart.urls', namespace='cart')),
    path('', include('shop.core.urls', namespace='core')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


