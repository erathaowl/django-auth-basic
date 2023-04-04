# coding=utf-8
from django.template.defaulttags import register

@register.filter(name='get_item')
def get_item(value, arg):
    return value.get(arg, None)
