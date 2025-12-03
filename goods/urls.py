from django.urls import include, path
from goods import views

app_name = 'catalog' # для атрібута namespace

urlpatterns = [
    # path('', views.catalog, name='index'),
    path('', views.GoodsListView.as_view(), name='index'),
    path('product/', views.product, name='product')
]