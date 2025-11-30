from django.urls import include, path
from . import views

app_name = 'catalog' # для атрібута namespace

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product')
]