from typing import Optional

from products.models import Product


def create_product(*, name: str, description: Optional[str], price: float) -> Product:
    price_in_cents = price * 100
    product = Product.objects.create(
        name=name, description=description, price=price_in_cents
    )
    return product


def delete_product(*, product: Product):
    product.delete()


def update_product(
    *, product: Product, name: str, description: Optional[str], price: float
) -> Product:
    product.name = name
    product.description = description
    product.price = price * 100
    product.save()

    return product
