from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from apps.core.models import Category, Product, Tag


def index(request):
    context = {}
    product_qs = Product.objects.order_by('-created_at')[:3]
    context['product_list'] = product_qs
    return render(request, 'core/index.html', context)


def category_list(request):
    context = {}
    category_qs = Category.objects.filter(title='some')

    context['category_list'] = category_qs
    return render(request, 'core/category_list.html', context)


def category_detail(request, slug):
    context = {}
    # category = Category.objects.filter(slug=slug).first()
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    return render(request, 'core/category.html', context)


def product_list(request):
    context = {}
    order = request.GET.get('order', '-created_at')
    search = request.GET.get('search', '')
    context['product_list'] = Product.objects.filter(
        title__icontains=search
    ).order_by(order)
    return render(request, 'core/product_list.html', context)


def product_detail(request, slug_category, pk):
    context = {}
    product = Product.objects.filter(
        pk=pk, category__slug=slug_category
    ).first()
    context['product'] = product
    return render(request, 'core/product.html', context)
