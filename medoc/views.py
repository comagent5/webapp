from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from medoc.models import MedocCodes


# Create your views here.
class MedocListView(ListView):
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

    def get_queryset(self):
        # 1. Отримати базовий (початковий) queryset
        if 'edrpo' in self.kwargs:
            edrpo = self.kwargs.get('edrpo')
            queryset = super().get_queryset().filter(edrpo=edrpo).order_by('date_cod')
            self.extra_context['title'] = f"Архів замовлень для ЄДРПОУ: {edrpo}"
        else:
            queryset = super().get_queryset()

        return queryset

    def get_context_data(self, **kwargs):
        # Виконання: 2-й етап (після get_queryset, paginate_queryset)
        # та перед передачею context у render для відображення шаблону

        # 1. Отримати стандартний контекст (включає відфільтрований self.object_list)
        context = super().get_context_data(**kwargs)

        # 2. Додавання іншої додаткової інформації (наприклад, загальна кількість знайдених ліцензій)
        context['total_count'] = context[self.context_object_name].count()

        return context