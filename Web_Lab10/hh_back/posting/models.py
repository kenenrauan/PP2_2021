from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    like_cnt = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





