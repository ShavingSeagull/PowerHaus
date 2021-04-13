from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def view_profile(request, username):
    """
    Function to render the public profile page. Viewable by anyone who 
    is currently logged in.
    """
    if str(username) == str(request.user):
        current_user = request.user
        userprofile = {
            "user": current_user,
            "first_name": current_user.first_name,
            "email": current_user.email,
            "date_joined": current_user.date_joined,
            "last_login": current_user.last_login,
            "location": current_user.profile.location,
            "bio": current_user.profile.bio
        }
    else:
        public_user = User.objects.get(username=username)
        userprofile = {
            "user": public_user,
            "first_name": public_user.first_name,
            "email": public_user.email,
            "date_joined": public_user.date_joined,
            "last_login": public_user.last_login,
            "location": public_user.profile.location,
            "bio": public_user.profile.bio
        }
    return render(request, "profiles/profile.html", context=userprofile)
