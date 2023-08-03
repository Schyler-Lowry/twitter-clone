"""
Schyler Lowry
CIS218
8/3/2023
"""
from django import template
register = template.Library()

@register.filter(name="subtract")
def subtract(value, arg):
    """subtracts the value by the arg"""
    return int(value) - int(arg)