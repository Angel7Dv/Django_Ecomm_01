from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail ,name='cart' ),

]
