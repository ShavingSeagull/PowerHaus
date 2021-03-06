from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import Profile
from .forms import ProfileForm
from promocodes.models import PromoCode
from checkout.models import Order, OrderLineItem


@login_required
def view_profile(request, username):
    """
    Function to render the public profile page. Viewable by anyone who
    is currently logged in.

    Will either render the user's own profile page (which will include
    editing options) or the page of another user, depending on which URL
    fires the function.
    """
    # Check if the username passed in matches the logged-in user
    if str(username) == str(request.user):
        current_user = request.user
        userprofile = {
            "user": current_user,
            "first_name": current_user.profile.first_name,
            "email": current_user.email,
            "date_joined": current_user.date_joined,
            "last_login": current_user.last_login,
            "location": current_user.profile.location,
            "bio": current_user.profile.bio
        }
    else:
        try:
            # Checks if user actually exists in the DB
            public_user = User.objects.get(username=username)
            userprofile = {
                "user": public_user,
                "first_name": public_user.profile.first_name,
                "email": public_user.email,
                "date_joined": public_user.date_joined,
                "last_login": public_user.last_login,
                "location": public_user.profile.location,
                "bio": public_user.profile.bio
            }
        except User.DoesNotExist:
            messages.error(request, "Sorry, that user doesn't seem to exist!")
            return redirect('home')
    return render(request, "profiles/profile.html", context=userprofile)


@login_required
def edit_profile(request, username):
    """
    Allows the user to edit their profile
    """
    # Check to see if the logged-in user is trying to edit someone else's page
    if str(username) != str(request.user):
        messages.error(request,
                       "Nice try, pal. You can only edit your own page!")
        return redirect('home')

    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile', username=username)
        else:
            messages.error(request,
                           "Failed to update. Please make sure the form was correct.")  # noqa: E501
    else:
        profile_form = ProfileForm(instance=profile)

    context = {
        "form": profile_form
    }

    return render(request, "profiles/profile_edit.html", context=context)


@login_required
def discount_page(request, username):
    """
    Displays all of the current active discounts
    """
    if str(username) != str(request.user):
        messages.error(request,
                       "Nice try, pal. You can only view your own discounts!")
        return redirect('home')

    now = timezone.now()
    discounts = PromoCode.objects.filter(start_date__lte=now,
                                         expiry_date__gte=now,
                                         active=True)
    context = {
        "discounts": discounts
    }

    return render(request, "profiles/profile_discounts.html", context=context)


@login_required
def order_history(request, username):
    """
    Displays all of the user's orders to date
    """
    if str(username) != str(request.user):
        messages.error(request,
                       "Nice try, pal. You can only view your own orders!")
        return redirect('home')

    now = timezone.now()
    user = get_object_or_404(Profile, user=request.user)
    orders = Order.objects.filter(user_profile=user).order_by('-date')

    context = {
        "orders": orders
    }
    return render(request, "profiles/profile_orders.html", context=context)


@login_required
def order_info(request, username, order_num):
    """
    Displays the detailed information of an individual order
    """
    if str(username) != str(request.user):
        messages.error(request,
                       "Nice try, pal. You can only view your own orders!")
        return redirect('home')

    order = get_object_or_404(Order, order_number=order_num)
    line_item = OrderLineItem.objects.filter(order=order)

    item_count = 0
    for item in line_item:
        item_count += item.quantity

    context = {
        "order": order,
        "line_item": line_item,
        "item_count": item_count
    }

    return render(request, "profiles/profile_orders_info.html",
                  context=context)
