from django.urls import path

from apps.api.v1.views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
)


urlpatterns = [
    path('product/', ProductCreateView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/all/', ProductListView.as_view()),
]
