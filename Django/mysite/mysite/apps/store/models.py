import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=200)
    product_description = models.TextField('Product Description')
    product_date = models.DateTimeField('Posted on', default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.product_name

    def was_posted_recently(self):
        return self.product_date >= (timezone.now() - datetime.timedelta(days=7))

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    auth_name = models.CharField('Author', max_length=50)
    comm_text = models.CharField("Text", max_length=200)

    def __str__(self):
        return self.auth_name