from django.shortcuts import render
from .cart import Cart
# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    productsstring = ""

    for item in cart:
        product = item['product']
        #url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s'}," % (product.id, product.title, product.price, item['quantity'])

        productsstring = productsstring + b
    ctx = {
        'cart':cart,
        'productsstring': productsstring
    }
    return render(request, 'cart/cart.html', ctx)