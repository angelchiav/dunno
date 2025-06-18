from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField()
    ROLES = [
        ('admin', 'Administrator'),
        ('ceo', 'CEO'),
        ('staff', 'Staff'),
        ('salesman', 'Salesman'),
        ('customer', 'Customer')
    ]
    role = models.CharField(max_length=8, choices=ROLES)

    def __str__(self):
        return self.name
    
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
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.order