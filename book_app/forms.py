from django import forms
from django.contrib.auth.models import User
from book_app.models import user, Sell

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ['firstname','lastname','email','phone','password']

class SellForm(forms.ModelForm):
    class Meta:
        model=Sell
        fields=['book_name','author','published_by','tags','types','price','pin_code','description','photo']
