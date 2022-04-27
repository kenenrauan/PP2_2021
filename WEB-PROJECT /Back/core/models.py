from django.db import models
from django.conf import settings
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'price': self.price
        }


class Review(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username.__str__(),
            'text': self.text
        }


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)


