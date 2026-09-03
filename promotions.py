from abc import ABC, abstractmethod

class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class SecondHalfPrice(Promotion):
    """Second item at half price"""
    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            quantity = quantity // 2
            return quantity * product.price + quantity * (product.price / 2)
        else:
            quantity = quantity // 2
            return quantity * product.price + quantity * (product.price / 2) + product.price

class ThirdOneFree(Promotion):
    """Every third item is free"""
    def apply_promotion(self, product, quantity):
        free_quantity = quantity // 3
        return (quantity - free_quantity) * product.price

class PercentDiscount(Promotion):
    """Discount the total price"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        return total_price - self.percent/100 * total_price
