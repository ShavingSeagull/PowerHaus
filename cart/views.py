from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """
    Displays the cart
    """
    return render(request, "cart/cart.html")

def add_to_cart(request):
    """
    Adds an item to the cart. The function is fired from the 
    product page, where the quantity is automatically set to 1. 
    This is then altered in the cart if the user wants more.
    """
    quantity = 1

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to
    the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))


def remove_from_cart(request, id):
    """
    Removes the selected item from the cart
    """
    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))
