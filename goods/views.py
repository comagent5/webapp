from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def catalog(request: HttpRequest):
    content = {
        'title': 'Мій перший WEB додаток',
        'goods': [
            '1-й товар',
            '2-й товар',
            '3-й товар',
            '4-й товар',
            '5-й товар',
            '6-й товар',
        ]
    }
    return render(request, 'goods/catalog.html', content)


def product(request: HttpRequest):
    content = {
        'title': 'Мій перший WEB додаток',
    }
    return render(request, 'goods/product.html', content)