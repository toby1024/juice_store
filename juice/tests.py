from django.test import TestCase

# Create your tests here.

from juice.models import Product, Category
from datetime import datetime 

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="fruit")
        Category.objects.create(name="juice")
      

    def test_category_name(self):
        """category show name"""
        fruit = Category.objects.get(name="fruit")
       
        self.assertEqual(fruit.name, 'fruit')


class ProductTestCase(TestCase):
  def setUp(self):
    category = Category.objects.create(name="fruit")
    Product.objects.create(name='fruit product', category=category, image='', description='描述', price=100.5, discount=90, )