from django.urls import path
from .views import view_profile, edit_profile, discount_page, order_history

urlpatterns = [
    path('<username>', view_profile, name="profile"),
    path('<username>/edit', edit_profile, name="edit_profile"),
    path('<username>/discounts', discount_page, name="discount_page"),
    path('<username>/orders', order_history, name="order_history")
]