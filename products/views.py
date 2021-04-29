from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve
from django.db.models import Q
from django.utils import timezone
from .models import Product
from reviews.models import Review

def products(request):
    """
    Displays the product list. Checks if the user entered a search term and, if so, 
    shows the search results. If not, it will render the products that match the URL 
    that fired the function as these match the product category names.
    """
    current_url = resolve(request.path_info).url_name
    products = Product.objects.filter(category__name=current_url).order_by('name')
    
    if request.GET:
        if 'q' in request.GET:
            search_query = request.GET['q']
            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            products = Product.objects.filter(queries).order_by('name')
            current_url = None
    
    context = {
        "products": products,
        "url": current_url
    }
    return render(request, "products/products_list.html", context=context)

def product_item(request, category, product_id):
    """
    Returns the selected item from the product list and displays its 
    details. Uses the product's category to maintain the appropriate 
    header image.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product, date__lte=timezone.now()).order_by('-date')
    good_total = 0
    bad_total = 0

    for score in reviews:
        if score.rating == "good":
            good_total += 1
        else:
            bad_total += 1

    context = {
        "product": product,
        "url": category,
        "reviews": reviews,
        "good_total": good_total,
        "bad_total": bad_total
    }
    return render(request, "products/products_item.html", context=context)
