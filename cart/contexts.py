from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from products.models import Product
from promocodes.models import PromoCode


def cart_contents(request):
    """
    Ensures that the cart contents are available
    when rendering every page. Also utilises the built-in
    Decimal function to handle the decimal numbers required for
    displaying monetary amounts. Quantize ensures the amounts
    remain human-readable.
    """

    cart = request.session.get('cart', {})
    code = request.POST.get('discount')
    if not code:
        code = request.session.get('discount', {})
        try:
            if cart == {}:
                del request.session['discount']
        except KeyError:
            # Ignore the error if the discount code doesn't exist
            pass

    now = timezone.now()

    cart_items = []
    discount_total = Decimal(0)
    subtotal = Decimal('0').quantize(Decimal('.01'))
    product_count = 0
    shipping = Decimal('1.20').quantize(Decimal('.01'))

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        price_by_quantity = Decimal(quantity) * Decimal(product.price)
        category = product.choice
        subtotal += price_by_quantity

        if code:
            try:
                promocode = PromoCode.objects.get(code__iexact=code,
                                                  start_date__lte=now,
                                                  expiry_date__gte=now,
                                                  active=True)

                # Promo Codes can target specific product groups, like Protein products, or all products
                # This checks if the Code type matches the product type, or whether it targets all products
                if promocode.product_type == category or promocode.product_type == 'all':
                    discount = Decimal((promocode.discount * price_by_quantity) / Decimal(100)).quantize(Decimal('.01'))
                    discount_total += discount

            except PromoCode.DoesNotExist:
                messages.error(request, "Promo Code is invalid")


        product_count += quantity
        request.session['discount'] = code

        cart_items.append({
                'id': id, 
                'quantity': quantity, 
                'product': product, 
                'item_total': price_by_quantity
                })

    # Shipping and total need to be outside the loop to avoid repeated additions that aren't necessary
    shipping *= product_count
    total = Decimal(subtotal - discount_total + shipping).quantize(Decimal('.01'))

    return {'cart_items': cart_items, 'subtotal': subtotal, 'discount_total': discount_total, 'shipping': shipping, 'total': total, 'product_count': product_count}