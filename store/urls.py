from django.urls import path
from .views import *
from .api import api_add_to_cart, api_remove_from_cart

urlpatterns = [

    path('<slug:category_slug>/<slug:slug>', product_detail ,name='product_detail' ),
    
    path('<slug:slug>', category_detail ,name='category_detail' ),


    #### [API] #####

    path('api/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove/', api_remove_from_cart, name='api_remove_from_cart')

]
