from django.urls import path

from apps.core.views import (
    index, category_list, category_detail, product_list, product_detail,
    contact_us,
    IndexView, IndexTemplateView, CategoryListView,
)

app_name = 'core'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug>/', category_detail, name='category-detail'),
    path('products/', product_list, name='product-list'),
    path('products/<slug_category>/<pk>/', product_detail, name='product-detail'),
    path('contact_us/', contact_us, name='contact-us'),
]
