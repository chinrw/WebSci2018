from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from lab4 import views

app_name = 'lab4'
urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
