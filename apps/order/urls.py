from django.urls import path

from apps.order.views import CartTemplateView, CartAddView

app_name = 'order'

urlpatterns = [
    path('cart/', CartTemplateView.as_view(), name='cart'),
    path('add/<pk>/', CartAddView.as_view(), name='cart-add'),
    # path('remove/<pk>/', RemoveCartView.as_view(), name='cart-remove'),
    # path('clear/', ClearCartView.as_view(), name='cart-clear'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
]
