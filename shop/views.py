from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import AddProductForm

def show_list(request):
    products = Product.objects.all()
    return render(request, 'shop/list.html', {'products':products})

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart})
