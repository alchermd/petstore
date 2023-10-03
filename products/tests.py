from django.test import TestCase
from django.urls import reverse

from products import services
from products.factory import ProductFactory
from products.models import Product

PRODUCT_DATA = {
    "name": "Special Dog",
    "description": "Premium grade dog food.",
    "price": 24.99,
}

NEW_PRODUCT_DATA = {
    "name": "Special Dog v2",
    "description": "The next version of the Special Dog product line.",
    "price": 29.50,
}


class ProductsServicesTests(TestCase):
    def setUp(self):
        super().setUp()

        self.product = Product.objects.create(
            name=PRODUCT_DATA["name"],
            description=PRODUCT_DATA["description"],
            price=PRODUCT_DATA["price"] * 100,
        )

    def test_can_create_new_product(self):
        product = services.create_product(**PRODUCT_DATA)

        self.assertEquals(product.name, PRODUCT_DATA["name"])
        self.assertEquals(product.description, PRODUCT_DATA["description"])
        self.assertEquals(product.price, PRODUCT_DATA["price"] * 100)

    def test_can_update_a_product(self):
        product = services.update_product(product=self.product, **NEW_PRODUCT_DATA)

        self.assertEquals(product.name, NEW_PRODUCT_DATA["name"])
        self.assertEquals(product.description, NEW_PRODUCT_DATA["description"])
        self.assertEquals(product.price, NEW_PRODUCT_DATA["price"] * 100)

    def test_can_delete_a_product(self):
        pk = self.product.pk

        services.delete_product(product=self.product)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(pk=pk)


class ProductsViewsTest(TestCase):
    def test_shows_a_notice_that_there_are_no_products(self):
        response = self.client.get(reverse("product-list"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No products yet.")

    def test_can_list_all_products(self):
        products = ProductFactory.create_batch(3)

        response = self.client.get(reverse("product-list"))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(products, response.context["products"])

    def test_can_create_a_new_product(self):
        response = self.client.post(reverse("product-create"), data=PRODUCT_DATA)
        self.assertRedirects(response, reverse("product-list"))
        self.assertEquals(1, Product.objects.all().count())

    def test_can_update_a_product(self):
        product = ProductFactory.create()

        response = self.client.post(reverse("product-update", args=[product.pk]), data=NEW_PRODUCT_DATA)
        self.assertRedirects(response, reverse("product-list"))

        product.refresh_from_db()
        self.assertEqual(product.name, NEW_PRODUCT_DATA["name"])
        self.assertEqual(product.description, NEW_PRODUCT_DATA["description"])
        self.assertEqual(product.price, NEW_PRODUCT_DATA["price"] * 100)

    def test_can_delete_a_product(self):
        product = ProductFactory.create()

        response = self.client.post(reverse("product-delete", args=[product.pk]), data={"confirm": True})
        self.assertRedirects(response, reverse("product-list"))

        with self.assertRaises(Product.DoesNotExist):
            product.refresh_from_db()
