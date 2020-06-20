from django.urls import path

from apps.core.views import (
    index, category_list, category_detail, product_list, product_detail
)

urlpatterns = [
    path('', index, name='index'),
    path('categories/', category_list, name='category-list'),
    path('categories/1/', category_detail, name='category-details'),
    path('products/', product_list, name='product-list'),
    path('products/notebooks/1', product_detail, name='product-detail'),
]
