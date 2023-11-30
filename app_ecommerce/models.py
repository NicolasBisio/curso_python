from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name}, {self.name}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - ${self.price}"

class Cart(models.Model):
    cart_user = models.CharField(max_length=100)
    products = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart of {self.cart_user}"