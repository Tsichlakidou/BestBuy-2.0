from typing import List
from products import Product


def order(shopping_list)-> float:
    """Make the order of the products."""
    total_price = 0
    for product, quantity in shopping_list:
        total_price += product.buy(quantity)
    return total_price


class Store:
    """Represent a store containing multiple products."""
    def __init__(self,products):
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self)->int:
        """Sum the quantity of all products in the store."""
        return sum([product.quantity for product in self.products])

    def get_all_products(self)->List[Product]:
        """Show all active products in the store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products
