from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    ctx = {
        'product' : product
        }
    return render(request, 'store/detail.html', ctx)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    ctx = {    
        'category' : category,
        'products': products
        }

    return render(request, 'store/category.html', ctx)


