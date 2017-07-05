from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product, Store
# Create your views here.

def products(request):
  product_list = Product.objects.filter(product_state = 1).order_by('-updated_at')
  return render(request, 'products.html', {'product_list': product_list})

def product(request, pk):
  return render(request, 'product.html', context={'product_detail': get_object_or_404(Product,pk=pk)})


def stores(request):
  store_list = Store.objects.filter(store_state = 1).order_by('-updated_at')
  return render(request, 'stores.html', {'store_list': store_list})

def about(request):
  return render(request, 'about.html')