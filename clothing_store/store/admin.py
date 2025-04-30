from django.contrib import admin
from .models import Category, Clothing, Cart, Order

admin.site.register(Category)
admin.site.register(Clothing)
admin.site.register(Cart)
admin.site.register(Order)
