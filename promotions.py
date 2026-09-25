"""Define promotion types for store products."""
from abc import ABC, abstractmethod

class Promotion(ABC):
    """Represent a base class for product promotions."""
    def __init__(self, name):
        """Initialize a promotion with a name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Apply the promotion and return the final price."""
        pass


class SecondHalfPrice(Promotion):
    """Second item at half price"""
    def apply_promotion(self, product, quantity):
        """Calculate the price with every second item at half price."""
        if quantity % 2 == 0:
            quantity = quantity // 2
            return quantity * product.price + quantity * (product.price / 2)
        quantity = quantity // 2
        return (
            quantity * product.price
            + quantity * (product.price / 2)
            + product.price
        )


class ThirdOneFree(Promotion):
    """Every third item is free"""
    def apply_promotion(self, product, quantity):
        """Calculate the price with every third item free."""
        free_quantity = quantity // 3
        return (quantity - free_quantity) * product.price


class PercentDiscount(Promotion):
    """Discount the total price"""
    def __init__(self, name, percent):
        """Initialize a percentage discount promotion."""
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Calculate the price with the given percent discount."""
        total_price = product.price * quantity
        return total_price - self.percent / 100 * total_price
