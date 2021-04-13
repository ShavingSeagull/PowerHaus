from django.urls import path
from .views import view_profile

urlpatterns = [
    path('<username>', view_profile, name="profile"),
    path('my-profile/edit'),
]