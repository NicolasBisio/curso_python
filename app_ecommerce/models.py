from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name}, {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Cart(models.Model):
    user = models.CharField(max_length=100)
    products = models.CharField(max_length=200)

    def __str__(self):
        return f"Cart of {self.user}"