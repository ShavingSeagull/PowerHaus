from django.shortcuts import render

def view_profile(request):
    return render(request, "profiles/profile_base.html")
