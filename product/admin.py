from django.contrib import admin
from .models import Category,SubCategory,ProductBrand,Product,ProductImage
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductBrand)
admin.site.register(Product)
admin.site.register(ProductImage)
