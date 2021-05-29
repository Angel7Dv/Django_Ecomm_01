from typing import ItemsView
from django.conf import settings


from store.models import Product

#settings.SESSION_COOKIE_AGEsettings.SESSION_COOKIE_AGE

#SESSION_COOKIE_AGE = 86400
#CART_SESSION_ID = 'cart'     

class Cart(object):
    def __init__(self, request):

        # el get de session es un dicciona rellenable
        self.session = request.session

        # Recuerda las cookies [dict]

        #[GET]
        cart = self.session.get(settings.CART_SESSION_ID)

        # Genera una nueva si no existe
        #[ADD]
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}


        # queda un simple diccionario que puede almacenar cookies

        self.cart = cart  #[1] {'1': {'quantity': 1, 'price': 98.3, 'id': '1'}}


    # [GET QUANTITY] conteo y suma de los totales de un producto

    def __iter__(self):
        products_ids = self.cart.keys() #[2] lista de objetos agregados = 
        products_clean_ids = []

        # AGREGA UN NUMERO Y UNA ID LIMPIA [{1 : ID}, {2 : ID}]
        for key in products_ids: #dict_keys(['1', '2'])

            products_clean_ids.append(key)
            #agrega un nuevo valor al dicccionario numero tal product: id
            self.cart[str(key)]['product'] = Product.objects.get(pk=key)


        # SUMA DE LOS TOTALES DE UN PRODUCTO
        for vdict in self.cart.values(): #{'quantity': 1, 'price': 98.3, 'id': '1'}}

            vdict['total_price'] = float(vdict['price']) * int(vdict['quantity'])
            yield vdict


    # SUMA LAS CANTIDADES DE PRODUCTOS
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())



    # [ADD] AGREGAR PRODUCTO AL CARRITO
    # TOMA EL MODEL PRODUCTO, LA CANTIDAD, Y ACCION SI ES ADD O UPDATE
    def add(self, model, cantidad=1, actualiza_cantidad=False):
 
        # Product.id = solo la instancia actual [variable agregada de for en el html]
        product_id = str(model.id)  

        # Product.price  # dato numerico
        price = model.price

        #[ADD] si no existe el objeto en el diccionario lo agrega

        if product_id is not self.cart:
            # add variable al dict = ### variable anteriro
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}
            print("test 1 ADD diccionario de session ", self.cart[product_id])

        #[UPDATE] si hay valor  de cantidad
        if actualiza_cantidad: # es true
            print("update true quantity")
            self.cart[product_id]['quantity'] = cantidad


        #[UPDATE] si no hay valor
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
            print("update false only add")

        self.save() # a continuacion se crea esta funcion



    # [DELETE]

    def remove(self, product_id):
        if product_id in self.cart:
            print("test 5 DELETE")

            del self.cart[product_id]
            self.save()



    # [SAVE]
    def save(self):


        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

        print("test 4 SAVE", self.cart)
