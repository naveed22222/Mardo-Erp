from django import template
from django.core.serializers import serialize
from django.core.paginator import Paginator

register = template.Library()
from datetime import datetime


# from num2words import num2words

@register.filter(name='convert_underscore')
def convert_underscore(value):
    return value.replace(' ', '_')


@register.filter(name='remove_underscore')
def remove_underscore(value):
    return value.replace('_', ' ')


@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg


@register.filter(name='add')
def subtract(value, arg):
    return value + arg


@register.filter(name='multiple')
def multiple(value, arg):
    return value * arg


@register.filter(name='divide')
def multiple(value, arg):
    return value / arg


@register.filter(name='numberFormat')
def numberFormat(value):
    return format(int(value), ',d')


@register.filter()
def to_int(value):
    return int(value)


@register.filter(name='abs')
def abs_filter(value):
    return abs(value)


@register.filter(name='abs')
def str_underscore(value):
    return abs(value)


@register.filter
def json(queryset):
    return serialize('json', queryset)


@register.filter(name='Shift')
def get_time_of_day(time):
    time = int(time)
    if time < 12:
        return "MOR"
    elif time < 19:
        return "EVN"


# @register.filter(name='NumberWord')
# def get_number_of_word(number):
#
#     get_word = num2words(number)
#     return get_word

@register.filter(name='SplitDash')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    dash_split = value.split(key)
    return dash_split[1]


@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=3, on_ends=2):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number,
                                           on_each_side=on_each_side,
                                           on_ends=on_ends)
