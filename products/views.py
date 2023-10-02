from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import reverse

from products import forms
from products import services
from products.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {"products": products})


def product_create(request):
    if request.method == "POST":
        form = forms.ProductCreateForm(request.POST)
        if form.is_valid():
            product = services.create_product(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
            )
            messages.success(request, f"{product.name} has been added to the system.")
            return redirect(reverse("product-list"))
    else:
        form = forms.ProductCreateForm()

    return render(request, "products/products_create.html", {"form": form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    initial_data = {
        "name": product.name,
        "description": product.description,
        "price": product.price / 100,
    }

    if request.method == "POST":
        form = forms.ProductUpdateForm(request.POST, initial=initial_data)

        if form.is_valid():
            product = services.update_product(
                product=product,
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
            )
            messages.success(request, f"{product.name} has been updated.")
            return redirect(reverse("product-list"))
    else:
        form = forms.ProductUpdateForm(initial=initial_data)

    return render(request, "products/products_update.html", {"form": form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = forms.ProductDeleteForm(request.POST)
        if form.is_valid():
            services.delete_product(product=product)
            messages.error(request, f"{product.name} has been deleted.")
            return redirect(reverse("product-list"))
    else:
        form = forms.ProductDeleteForm()

    return render(request, "products/products_delete.html", {"form": form})
