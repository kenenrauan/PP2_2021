from .models import Category, Product
from django.contrib import admin

admin.site.register((Product, Category))