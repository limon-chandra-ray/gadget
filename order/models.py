from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    class StatusRole(models.TextChoices):
        INCOMPLETED = 'INCOMPLETED','Incompleted'
        COMPLETED = 'COMPLETED','Completed'
        PENDING = 'PENDING', 'Pending'
        HOLD = 'HOLD','Hold'
        PROCESSING = 'PROCESSING', 'Processing'
    default_status = StatusRole.INCOMPLETED
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    order_status = models.CharField(max_length=50,choices=StatusRole.choices,null=True,blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(max_length=150,null= True,blank=True,unique=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    

    def __str__(self):
        return self.user.username
    
    @property
    def get_order_total_amount(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_order_total_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total
    


class OrderAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    address = models.TextField()
    district = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    