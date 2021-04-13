from django.urls import path
from .views import view_profile, edit_profile

urlpatterns = [
    path('<username>', view_profile, name="profile"),
    path('<username>/edit', edit_profile, name="edit_profile"),
]