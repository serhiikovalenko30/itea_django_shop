from django.views.generic import View, TemplateView, RedirectView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from apps.core.models import Product
from apps.order.cart import Cart
from apps.order.models import OrderProduct
from apps.order.forms import OrderForm


class CartTemplateView(TemplateView):
    template_name = 'order/cart.html'


class CartAddView(View):

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        cart = Cart(request)
        cart.add(product)
        return redirect('core:product-list')
