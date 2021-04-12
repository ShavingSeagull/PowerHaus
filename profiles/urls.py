from django.urls import path
from .views import view_profile

urlpatterns = [
    path('<user>', view_profile, name="profile"),
]