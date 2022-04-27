from django.contrib import admin
from core.models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass