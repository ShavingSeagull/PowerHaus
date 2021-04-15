from django.shortcuts import render
from django.urls import resolve
from .models import Product

def products(request):
    """
    Uses the url to filter the products shown by category
    """
    current_url = resolve(request.path_info).url_name
    products = Product.objects.filter(category__name=current_url).order_by('name')
    context = {
        "products": products
    }
    return render(request, "products/products_list.html", context=context)
