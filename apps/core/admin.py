from django.contrib import admin

# from .models import Product
from apps.core.models import Category, Tag, Product


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
