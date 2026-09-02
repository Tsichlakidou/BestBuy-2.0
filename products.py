class Product:
    """Represent a product available in the store."""
    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self)-> int:
        """Return the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the current product quantity."""
        self.quantity = quantity
        if self.quantity ==0:
            self.deactivate()

    def is_active(self) -> bool:
        """Is the product active or not."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Show the product."""
        print(self.name, "Price:",self.price, "Quantity:", self.quantity)

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        if quantity > self.quantity:
            raise Exception("There are not enough products for this purchase")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    """Represent a non-stored product available in the store."""
    def __init__(self,name, price):
        super().__init__(name, price, 0)

    def show(self):
        """Show the product."""
        print(self.name, "Price:", self.price)

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity <= 0:
            raise Exception("Quantity must be positive")
        return self.price * quantity

class LimitedProduct(Product):
    """Represent a limited product available in the store."""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Show the product."""
        super().show()
        print("Maximum:", self.maximum)

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity > self.maximum:
            raise Exception(f"You can only buy {self.maximum} products")
        return super().buy(quantity)
