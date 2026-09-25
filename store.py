"""Define the Store class and order functionality."""
from typing import List
from products import Product


class Store:
    """Represent a store containing multiple products."""
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Sum the quantity of all products in the store."""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Show all active products in the store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """Make the order of the products."""
        combined_order = {}
        original_quantities = {}
        for product, quantity in shopping_list:
            if product in combined_order:
                combined_order[product] += quantity
            else:
                combined_order[product] = quantity
                original_quantities[product] = product.get_quantity()
        try:
            total_price = 0
            for product, quantity in combined_order.items():
                total_price += product.buy(quantity)
        except Exception:
            for product, original_quantity in original_quantities.items():
                product.set_quantity(original_quantity)

            raise
        return total_price
