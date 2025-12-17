from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from medoc.models import MedocCodes


# Create your views here.
class MedocListView(LoginRequiredMixin, ListView):
    """
    Класс: БД замовлень кодів доступу (ліцензій) М.Е.Док
    """
    model = MedocCodes
    template_name = 'medoc/medoc_codes.html'
    context_object_name = 'medoc_codes'
    extra_context = {
        'title': 'Архів замовлень кодів доступу (ліцензій) М.Е.Док',
    }
    paginate_by = 15
    # Список назв полів, які ми хочемо бачити в таблиці (по порядку)
    field_names = [
        'edrpo', 'name', 'date_cod', 'type_cod',
        'sum_cl', 'sum_diler', 'date_zakaz',
        'module', 'sum_comp', 'note'
    ]

    def get_queryset(self):
        # 1. Отримати базовий (початковий) queryset
        queryset = super().get_queryset()

        # 2. Пошу по ЄДРПОУ
        edrpo = self.kwargs.get('edrpo', '')
        if not edrpo:
            edrpo = self.request.GET.get('edrpo', '')
        if edrpo:
            self.extra_context['edrpo'] = edrpo
            queryset = super().get_queryset().filter(edrpo=edrpo).order_by('date_cod')
            self.extra_context['title'] = f"Архів замовлень для ЄДРПОУ: {edrpo}"

        return queryset

    def get_context_data(self, **kwargs):
        # Виконання: 2-й етап (після get_queryset, paginate_queryset)
        # та перед передачею context у render для відображення шаблону

        # 1. Отримати стандартний контекст (включає відфільтрований self.object_list)
        context = super().get_context_data(**kwargs)

        # Отримуємо МЕТА-дані моделі
        opts = self.model._meta
        # Створюємо список заголовків (verbose_name)
        context['table_headers'] = [
            opts.get_field(name).verbose_name for name in self.field_names
        ]

        # Щоб у циклі <tbody> було зручно виводити дані,
        # збережемо також імена полів
        context['field_names'] = self.field_names

        # 2. Додавання значення ЄДРПОУ для фільтру
        context['edrpo'] = self.request.GET.get('edrpo', '')

        return context