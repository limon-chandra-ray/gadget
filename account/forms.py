from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # phone_no = forms.CharField(max_length = 20)
    # first_name = forms.CharField(max_length = 20)
    # last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        exclude = ['user']