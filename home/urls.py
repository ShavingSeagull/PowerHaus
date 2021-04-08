from django.urls import path
from .views import index, about, delivery_info, contact

urlpatterns = [
    path('', index, name="home"),
    path('about', about, name="about"),
    path('delivery-infomation', delivery_info, name="delivery_info"),
    path('contact', contact, name="contact")
]