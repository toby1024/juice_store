from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name

class Store(models.Model):
  name = models.CharField(max_length=40)
  link_man = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)
  address = models.CharField(max_length=200)
  store_state = models.IntegerField()
  level = models.IntegerField()
  image = models.ImageField(upload_to = 'stores')
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def alive(self):
    return self.store_state == 1

  def __str__(self):
    return (self.name + ':' + self.address).encode('utf8')

class Product(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  price = models.FloatField()
  discount = models.IntegerField()
  image = models.ImageField(upload_to = 'products')
  product_state = models.IntegerField()
  category = models.ForeignKey(Category)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def alive(self):
    return self.product_state == 1

  def discount_price(self):
    return self.price*self.discount/100

  def __str__(self):
    return (self.name + ":" + self.category.name).encode('utf8')

class Customer(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=30)
  sex = models.IntegerField()
  birthday = models.DateField()
  vip = models.IntegerField()
  customer_state = models.IntegerField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def get_absolute_url(self):
    return reverse('juice:product', kwargs={'pk': self.pk}) 

  def is_vip(self):
    return self.vip == 1

class PayType(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name.encode('utf8')

class Order(models.Model):
  order_number = models.CharField(max_length=10)
  customer = models.ForeignKey(Customer)
  product = models.ForeignKey(Product)
  amount = models.FloatField()
  discount = models.IntegerField()
  payed = models.FloatField()
  pay_type = models.ForeignKey(PayType)
  order_state = models.IntegerField()
  store = models.ForeignKey(Store)
  saler = models.ForeignKey(User)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def is_payed(self):
    return self.payed == 1

  def is_overdue(self):
    return self.order_state == 2

  def is_success(self):
    return self.order_state == 1
