from django.urls import path
from reviews.views import add_review, edit_review, delete_review
from .views import products, product_item

urlpatterns = [
    path('protein', products, name="protein"),
    path('vitamins', products, name="vitamins"),
    path('supplements', products, name="supplements"),
    path('equipment', products, name="equipment"),
    path('<category>/<product_id>', product_item, name="product_item"),
    path('<category>/<product_id>/add_review', add_review, name="add_review"),
    path('<category>/<product_id>/edit_review/<review_id>', edit_review,
         name="edit_review"),
    path('<category>/<product_id>/delete_review/<review_id>', delete_review,
         name="delete_review")
]
