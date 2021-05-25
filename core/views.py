from django.shortcuts import render
from store.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()

    ctx = {
        'products' : products
    }

    return render(request, 'core/index.html', ctx)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')