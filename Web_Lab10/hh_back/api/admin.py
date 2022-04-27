from django.contrib import admin
from .models import Company
from .models import Vacancy

admin.site.register(Company)


@admin.register(Vacancy)
class VacAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')