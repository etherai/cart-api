from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name="addresses")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)


class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    our_price = models.DecimalField(max_digits=10, decimal_places=2)
    origianl_url = models.TextField()
    image_url = models.TextField()
    html = models.TextField()
    options = models.TextField()
    imageData = models.TextField()

 
class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('auth.User', related_name="carts")
    items = models.ManyToManyField(Product)    


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True)
    items = models.ManyToManyField(Product) 
    user = models.ForeignKey('auth.User', related_name="orders")
