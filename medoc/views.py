from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from medoc.models import MedocCodes


# Create your views here.
class MedocListView(ListView):
    """
    Класс: БД кодів доступу (ліцензій) М.Е.Док
    """
    model = MedocCodes
    template_name = 'medoc/medoc_codes.html'
    context_object_name = 'medoc_codes'
    extra_context = {
        'title': 'БД кодів доступу (ліцензій) М.Е.Док',
    }

    def get_queryset(self):
        # 1. Отримати базовий (початковий) queryset
        queryset = super().get_queryset()

        return queryset
