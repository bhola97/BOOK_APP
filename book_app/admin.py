from django.contrib import admin
from .models import user,Sell, Cart
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(user)
# admin.site.register(Tag)
admin.site.register(Sell)
admin.site.register(Cart)
