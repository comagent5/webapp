from django import template

register = template.Library()

@register.filter
def get_attribute(value, arg):
    """Отримує атрибут об'єкта динамічно (як getattr)"""
    return getattr(value, arg, "")