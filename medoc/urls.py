from django.urls import path, re_path
from medoc import views

app_name = 'medoc' # для атрібута namespace

urlpatterns = [
    re_path(r'^(P<edrpo>\d{8, 10})/', views.MedocListView.as_view(), name='medoc_edrpo'),
    path('', views.MedocListView.as_view(), name='medoc_codes'),

]