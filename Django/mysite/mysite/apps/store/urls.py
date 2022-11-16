from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.start, name='start'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)