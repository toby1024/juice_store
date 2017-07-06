from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product, Store
# Create your views here.

def index(request):
  return products(request, 1)

def products(request, page):
  request.session['custom'] = 'custom_name'
  page_size = 18
  product_list = Product.objects.filter(product_state = 1).order_by('-updated_at')
  total_count = product_list.count()
  total_page = total_count/page_size if total_count%page_size==0 else int(total_count/page_size)+1
  offset = ((int(page)-1)*page_size)
  product_list = product_list[offset:(page_size+offset)]
  return render(request, 'products.html', {'product_list': product_list, 'total_count': total_count, 'total_page': range(1, total_page+1), 'current_page': int(page)})

def product(request, pk):
  return render(request, 'product.html', {'product_detail': get_object_or_404(Product,pk=pk)})


def stores(request):
  store_list = Store.objects.filter(store_state = 1).order_by('-updated_at')
  return render(request, 'stores.html', {'store_list': store_list})

def about(request):
  return render(request, 'about.html')