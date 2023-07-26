from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save,sender = User)
def create_client_profile(sender,instance,created,*args, **kwargs):
    if created:
        ClientProfile.objects.create(user = instance)

# Create your models here.
class ClientProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    post_code = models.IntegerField(null=True,blank=True)