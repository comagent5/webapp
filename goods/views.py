from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from goods.models import Category, Product

# Create your views here.
def catalog(request: HttpRequest):
    categories = Category.objects.all()

    content = {
        'title': 'Мій перший WEB додаток',
        'categories': categories,
    }
    return render(request, 'goods/catalog.html', content)


class GoodsListView(ListView):
    """
    Каталог товарів
    """
    model = Product # --- Якщо потрібно відобразити всі записи з модулі, або
    # queryset = Product.objects.all()

    # Задаємо ім'я файла шаблону
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'Мій перший WEB додаток',
    }

    # Задаємо кастомізований queryset
    # def get_queryset(self):
    #    return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Обробка параметрів з kwargs (з URL)


def product(request: HttpRequest):
    content = {
        'title': 'Мій перший WEB додаток',
    }
    return render(request, 'goods/product.html', content)