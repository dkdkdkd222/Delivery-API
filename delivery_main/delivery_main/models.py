from django.db import models




class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=150)
  email = models.EmailField(max_length=100)
  about_them = models.TextField(blank=True, null=True)
  phone_number = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)


class Item(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  item_name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  item = models.ManyToManyField(Item, related_name = 'orders')
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, choices = [
    ('PENDING', 'Pending'), 
    ('IN_PROGRESS', 'In Progress'),
    ('DISPATCHED', 'Dispatched'),
    ('UNABLE_TO_DELIVER', 'Unable to Deliver'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
  ], default = 'PENDING')
  delivery_address = models.TextField(blank=True, null=True)