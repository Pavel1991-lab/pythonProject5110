from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)  # наименование
    description = models.TextField()  # описание
    image = models.ImageField(upload_to='product_images')  # изображение (превью)
    category = models.CharField(max_length=100)  # категория как строка
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # цена за покупку
    created_date = models.DateTimeField(auto_now_add=True)  # дата создания
    last_modified_date = models.DateTimeField(auto_now=True)  # дата последнего изменения

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.CharField(max_length=19)
