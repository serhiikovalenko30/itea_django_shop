from django import template

from apps.core.models import Contacts

register = template.Library()


@register.inclusion_tag('components/footer.html')
def footer():
    context = {}
    contact = Contacts.load()
    context['contact'] = contact
    context['address'] = contact.address
    context['phone'] = contact.phone
    return context
