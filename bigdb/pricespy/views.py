from django.shortcuts import render
from .models import one_product

# Create your views here.

def product_list(request):
	products = one_product.objects.all()
	return render(request, 'pricespy/product_list.html', {'products':products})
