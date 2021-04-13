from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request, user):
    """
    Function to render the profile page. Requires login.
    """
    return render(request, "profiles/profile.html")
