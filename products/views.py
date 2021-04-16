from django.shortcuts import render, redirect
from django.urls import resolve
from django.db.models import Q
from .models import Product

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
    
    context = {
        "products": products
    }
    return render(request, "products/products_list.html", context=context)
