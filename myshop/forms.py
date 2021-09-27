from django  import forms
from django.forms import fields
from .models import Order
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class Myorder(forms.ModelForm):
    class Meta:
        model=Order
        exclude=["user", ]
    

class Customusercreation(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [ "username","first_name", "last_name",
                  "email", "password1", "password2"]
        

class Customerlogin(AuthenticationForm):
    class Meta:
        model=User
        fields="__all__"