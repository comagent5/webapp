from django import template
from django.urls import reverse

register = template.Library()

@register.filter
def get_attribute(value, arg):
    """Отримує атрибут об'єкта динамічно (як getattr),
    щоб значення x_val = value[arg], можно було використати як змінну {{ x_val }}
    в шаблоні
    """
    return getattr(value, arg, "")


@register.simple_tag(takes_context=True)
def active_link(context, url_name, css_class='active'):
    """
    Використовується для позначення поточного пункта меню.
    Повертає заданий css класс (за замовченням 'active'), якщо поточний end-point (path)
    співпадає с заданим url_name.
    :param context:
    :param url_name:
    :param css_class:
    :return: css_class або порожній рядок
    """
    # Отримуємо поточний шлях
    request = context.get('request')
    if request:
        current_path = request.path
        # Отримуємо шлях посилання по його імені
        target_path = reverse(url_name)
        if current_path == target_path:
            return css_class
    return ''