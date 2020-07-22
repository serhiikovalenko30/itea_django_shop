from rest_framework import generics

from apps.api.v1.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
)
from apps.core.models import Product


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
