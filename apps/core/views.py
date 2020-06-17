from django.shortcuts import render

from apps.core.models import Category, Product, Tag


def index(request):
    context = {}

    return render(request, 'index.html', context)
