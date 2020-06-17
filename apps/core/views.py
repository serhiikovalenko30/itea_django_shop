from django.shortcuts import render

from apps.core.models import Category, Product, Tag


def index(request):
    category_qs = Category.objects.all()
    product_qs = Product.objects.order_by('-title')
    context = {
        'category_list': category_qs,
        'product_list': product_qs
    }

    # for category in category_qs:
    #     print('category', category.title)
    #     for product in category.product_set.all():
    #         print(product.title)

    return render(request, 'index.html', context)
