from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def products(request):
  product_list = Product.objects.filter(product_state = 1)
  return render(request, 'products.html', {'product_list': product_list})

def product(request, pk):
  return render(request, 'product.html', context={'product_detail': get_object_or_404(Product,pk=pk)})
