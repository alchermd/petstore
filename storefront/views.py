from django.shortcuts import render

from products.models import Product


def storefront(request):
    products = Product.objects.all()
    return render(request, "storefront/index.html", {"products": products})
