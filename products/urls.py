from django.urls import path
from .views import products, product_item

urlpatterns = [
    path('protein', products, name="protein"),
    path('vitamins', products, name="vitamins"),
    path('supplements', products, name="supplements"),
    path('equipment', products, name="equipment"),
    path('<category>/<product_id>', product_item, name="product_item"),
]