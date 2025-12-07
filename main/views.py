from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    content = {
        'title': 'Мій перший WEB додаток',
        'h1': 'Головна сторінка',
        'content': 'Контент головної сторінки',
        'list': ['one', 'two', 'three'],
        'dict': {
            1: 'one',
            2: 'two'},
        'bool': True,
    }
    return render(request, 'main/index.html', content) 


@login_required(login_url='users:login')
def about(request: HttpRequest) -> HttpResponse:
    content = {
        'title': 'Мій перший WEB додаток',
    }
    return render(request, 'main/about.html', content)