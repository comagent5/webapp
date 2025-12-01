from django.http import HttpRequest
from django.shortcuts import render
from goods.models import Category

# Create your views here.
def catalog(request: HttpRequest):
    categories = Category.objects.all()

    content = {
        'title': 'Мій перший WEB додаток',
        'categories': categories,
    }
    return render(request, 'goods/catalog.html', content)


def product(request: HttpRequest):
    content = {
        'title': 'Мій перший WEB додаток',
    }
    return render(request, 'goods/product.html', content)