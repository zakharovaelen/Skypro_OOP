import pytest

from Product import Product
from 14.1_main import Category

@pytest.fixture

def first_product():
    return Product(
        name="name",
        description="description",
        price="price",
        quantity="quantity",
    )


