from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart

urlpatterns = [
    path('your-cart', view_cart, name="cart"),
    path('add-to-cart/<id>', add_to_cart, name="add_to_cart"),
    path('adjust-cart/<id>', adjust_cart, name="adjust_cart"),
    path('remove-from-cart/<id>', remove_from_cart, name="remove_from_cart")
]
