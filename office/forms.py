from django import forms
from product.models import ProductBrand,Category,SubCategory,Product,ProductImage
class ProductBrandFrom(forms.ModelForm):
    class Meta:
        model= ProductBrand
        fields = '__all__'

class CategoryFrom(forms.ModelForm):
    class Meta:
        model= Category
        fields = '__all__'

class SubCategoryFrom(forms.ModelForm):
    class Meta:
        model= SubCategory
        fields = '__all__'


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class ProductImageFrom(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image','image_name']