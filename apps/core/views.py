from django.shortcuts import render, get_object_or_404

from apps.core.models import Category, Product, Tag


def index(request):
    context = {}
    category_qs = Category.objects.all()
    product_qs = Product.objects.order_by('-title')[:3]

    context['category_list'] = category_qs
    context['product_list'] = product_qs
    return render(request, 'core/index.html', context)


def category_list(request):
    context = {}
    return render(request, 'core/category_list.html', context)


def category_detail(request, slug):
    context = {}
    # category = Category.objects.filter(slug=slug).first()
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    # category.views += 1
    # category.save()
    return render(request, 'core/category.html', context)


def product_list(request):
    context = {}
    return render(request, 'core/product_list.html', context)


def product_detail(request, slug_category, pk):
    context = {}
    product = Product.objects.filter(
        pk=pk, category__slug=slug_category
    ).first()
    context['product'] = product
    return render(request, 'core/product.html', context)
