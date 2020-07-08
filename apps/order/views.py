from django.views.generic import View, TemplateView, RedirectView
from django.views.generic import View, RedirectView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from apps.core.models import Product
from apps.order.cart import Cart
from apps.order.models import OrderProduct
from apps.order.forms import OrderForm
