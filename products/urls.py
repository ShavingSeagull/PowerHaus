from django.urls import path
from .views import products

urlpatterns = [
    path('protein', products, name="protein"),
]