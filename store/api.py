from django.http.response import JsonResponse

import json

from django.shortcuts import get_object_or_404

from cart.cart import Cart

from .models import Product

def api_add_to_cart(request):
    ############
    data = json.loads(request.body)
    

    ###################
    #estos datos de momento no se usan
    jsonresponse = {'success': True}

    #   datos para ser usados en la logica del html
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']



    # objeto dict cookie recien creado
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    # VARIABLES
    #print(cart.cart)   # ==> {'1': {'quantity': 1, 'price': 98.3, 'id': '1'}}
    #print(cart.cart.keys())  # ==> el 1
    #print(cart.cart.values())  # ==> {'quantity': 1, 'price': 98.3, 'id': '1'}}


    # [ADD] crea el objeto y lo guarda
    if not update:
        #la funcion dentro del diccionario cookie
        cart.add(model=product, cantidad=1, actualiza_cantidad=False)
        print("update false")


    # [UPDATE] aumenta la cantidad asignada
    else:
        cart.add(model=product, cantidad=quantity , actualiza_cantidad=True)
        print("add quantity")
        
    return JsonResponse(jsonresponse)



# API REMOVE

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id']) 
    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)