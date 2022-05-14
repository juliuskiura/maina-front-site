from django.urls import path
from .views import *


urlpatterns = [
 # post views

 path('price/', get_price, name = 'getprice'),
 

]