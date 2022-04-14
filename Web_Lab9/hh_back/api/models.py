from django.db import models
from django.db.models import CharField, FloatField, TextField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    city = models.CharField(max_length=255)
    address = models.TextField(default='')
    
    class Meta:
        verbose_name_plural = 'Companies'
    
    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    salary = models.FloatField(default=0)
    company = ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            # 'company': self.company,
    }
    
    def __str__(self):
        return f'{self.name} | {str(self.company)}'