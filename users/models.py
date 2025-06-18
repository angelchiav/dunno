from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLES = [
        ('admin', 'Administrator'),
        ('ceo', 'CEO'),
        ('staff', 'Staff'),
        ('salesman', 'Salesman'),
        ('customer', 'Customer')
    ]
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=8, choices=ROLES, default='customer')

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else self.username
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} - {self.customer.first_name}'

class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Shipping for order {self.order.id}'