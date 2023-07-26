from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    image = models.FileField(upload_to='category',blank=True,null=True)
    status = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class ProductBrand(models.Model):
    name = models.CharField(max_length=250,unique=True)
    image = models.FileField(upload_to='brand',null=True,blank=True)
    status = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.BigIntegerField()
    offer_price = models.FloatField()
    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE)
    image = models.FileField(upload_to='product/',null=True,blank=True)
    discreption = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.FileField(upload_to='product/')
    image_name = models.CharField(max_length=250)

    def __str__(self):
        return self.image_name
    