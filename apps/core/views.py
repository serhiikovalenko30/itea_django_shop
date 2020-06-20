from django.shortcuts import render

from apps.core.models import Category, Product, Tag


def index(request):
    context = {}
    category_qs = Category.objects.all()
    product_qs = Product.objects.order_by('-title')

    context['category_list'] = category_qs
    context['product_list'] = product_qs
    return render(request, 'core/index.html', context)


def category_list(request):
    context = {}
    return render(request, 'core/category_list.html', context)


def category_detail(request):
    context = {}
    return render(request, 'core/category.html', context)


def product_list(request):
    context = {}
    return render(request, 'core/product_list.html', context)


def product_detail(request):
    context = {}
    return render(request, 'core/product.html', context)
