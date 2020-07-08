from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from apps.core.forms import ContactUsModelForm
from apps.core.models import Category, Product


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


def contact_us(request):
    context = {}

    if request.method == 'POST':
        form = ContactUsModelForm(request.POST)
        # form = ContactUsModelForm({
        #     'name': request.POST.get('name'),
        #     'user': request.user
        # })
        if form.is_valid():
            contactus_obj = form.save(commit=False)
            contactus_obj.email = 'some@test.test'
            contactus_obj.save()
            return HttpResponseRedirect('/')
        else:
            return JsonResponse(form.errors)
    else:
        form = ContactUsModelForm()

    context['form'] = form
    return render(request, 'core/contact_us.html', context)
