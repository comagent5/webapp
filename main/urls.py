from django.urls import include, path
from . import views

app_name = 'main' # для атрібута namespace

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about')
]