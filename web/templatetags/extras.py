
# web/templatetags/extras.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary and key:
        return dictionary.get(key, "")
    return ""

@register.filter
def prettify_status(value):
    """Convert STATUS_CODE into a human readable form"""
    if not value:
        return ""
    return value.replace("_", " ").title()
