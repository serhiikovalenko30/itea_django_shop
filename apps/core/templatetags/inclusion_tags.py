from django import template

from apps.core.models import Category, Contacts

register = template.Library()


@register.inclusion_tag('components/footer.html')
def footer():
    context = {}
    contact = Contacts.load()
    context['address'] = contact.address
    context['phone'] = contact.phone
    return context


@register.inclusion_tag('components/header.html')
def header():
    context = {}
    context['category_list'] = Category.objects.all()
    return context


@register.inclusion_tag('core/components/category_list.html')
def category_list():
    category_qs = Category.objects.all()
    return {'category_list': category_qs}
