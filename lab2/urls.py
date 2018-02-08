from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from lab2 import views

app_name = 'lab2'
urlpatterns = [
    path('', views.index, name='index'),
    path('weather', views.weather, name='weather')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
