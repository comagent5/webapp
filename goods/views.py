from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

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

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    # Обробка параметрів з kwargs (з URL)


def product(request: HttpRequest):
    content = {
        'title': 'Мій перший WEB додаток',
    }
    return render(request, 'goods/product.html', content)


class ShowProduct(DetailView):
    # model = Product
    context_object_name = 'product'
    template_name = 'goods/product.html'
    slug_url_kwarg = 'prod_slug'
    pk_url_kwarg = 'prod_pk'
    extra_context = {
        'title': 'Мій перший WEB додаток',
    }

    def get_object(self, queryset = None):
        if self.slug_url_kwarg in self.kwargs:
            return get_object_or_404(Product, slug=self.kwargs[self.slug_url_kwarg])
        elif self.pk_url_kwarg in self.kwargs:
            return get_object_or_404(Product, pk=self.kwargs[self.pk_url_kwarg])
        return None