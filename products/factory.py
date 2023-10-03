import factory
from factory.django import DjangoModelFactory


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = "products.Product"

    name = factory.Faker("word")
    description = factory.Faker("paragraph")
    price = factory.Faker("random_int", min=99, max=99999)
