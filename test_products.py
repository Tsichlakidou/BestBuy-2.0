import pytest
from products import Product

def test_create_normal_product():
    product = Product("MacBook", 1450, 100)

    assert product.get_quantity() == 100
    assert product.price == 1450
    assert product.name == "MacBook"

def test_invalid_product_details():
    with pytest.raises(Exception):
        Product("", 1450, 100)
    with pytest.raises(Exception):
        Product("Mac", -1450, 100)

def test_inactivating_product():
    product = Product("MacBook", 1450, 100)
    product.set_quantity(0)
    assert product.is_active() == False

def test_purchase_product():
    product = Product("MacBook", 1450, 100)
    assert product.buy(10) == 14500
    assert product.get_quantity() == 90

def test_not_enough_quantity():
    product = Product("MacBook", 1450, 100)
    with pytest.raises(Exception):
        product.buy(101)
