from django.urls import include, path
from goods import views

app_name = 'catalog' # для атрібута namespace

urlpatterns = [
    # path('', views.catalog, name='index'),
    path('', views.GoodsListView.as_view(), name='index'),
    # path('product/', views.product, name='product'),
    path('<int:prod_pk>/', views.ShowProduct.as_view(), name='product'),
    path('<slug:prod_slug>/', views.ShowProduct.as_view(), name='product'),
]