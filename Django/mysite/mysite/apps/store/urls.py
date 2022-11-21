from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('premium/', views.premium, name='premium'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)