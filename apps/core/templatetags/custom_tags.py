from django import template

from apps.core.models import Contacts

register = template.Library()


@register.simple_tag(takes_context=True)
def get_title(context, param, text):
    contact = Contacts.load()
    return contact.title
