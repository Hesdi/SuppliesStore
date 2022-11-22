from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('adding/', views.adding, name='adding'),
    path('adding/add_product', views.add_product, name='add_product'),
    path('test/', views.test, name='test'),
    path('premium/', views.premium, name='premium'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]