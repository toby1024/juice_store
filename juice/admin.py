from django.contrib import admin
from .models import Product, Store, Category, PayType, Order, Customer
# Register your models here.

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(PayType)
admin.site.register(Order)
admin.site.register(Customer)