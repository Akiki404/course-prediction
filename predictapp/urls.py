from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'predictapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('database/', views.database, name='db'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)