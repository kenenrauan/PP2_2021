from .models import Company, Vacancy
from django.contrib import admin

admin.site.register((Company, Vacancy))