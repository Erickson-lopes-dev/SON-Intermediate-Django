
from django.urls import path

from .views import *


app_name = 'my_app'
urlpatterns = [
    path('login/', login),
    path('', address_list),
    path('logout/', logout),
    path('home/', home),
    path('addresses/', address_list, name='address_list'),
    path('addresses/create/', address_create, name='address_create'),
    path('addresses/<int:id>/update/', address_upate, name='address_update'),
]

