"""Define the product classes for the Best Buy store."""
class Product:
    """Represent a product available in the store."""
    def __init__(self, name, price, quantity, promotion=None):
        if name == "":
            raise Exception("Name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = promotion

    def get_quantity(self) -> int:
        """Return the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the current product quantity."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def get_promotion(self):
        """Return the current product promotion."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set the current product promotion."""
        self.promotion = promotion

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
        if self.promotion is None:
            print(self.name, "Price:", self.price, "Quantity:", self.quantity)
        else:
            print(
                self.name,
                "Price:", self.price,
                "Quantity:", self.quantity,
                "Promotion:", self.promotion.name
            )

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        if quantity > self.quantity:
            raise Exception("There are not enough products for this purchase")

        self.set_quantity(self.quantity - quantity)

        if self.get_promotion() is None:
            return self.price * quantity
        return self.promotion.apply_promotion(self, quantity)


class NonStockedProduct(Product):
    """Represent a non-stored product available in the store."""
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.activate()

    def set_quantity(self, quantity):
        """Do not change quantity for a non-stocked product."""
        pass

    def show(self):
        """Show the product."""
        if self.promotion is None:
            print(self.name, "Price:", self.price, "Quantity: Unlimited")
        else:
            print(
                self.name,
                "Price:", self.price,
                "Quantity: Unlimited",
                "Promotion:", self.promotion.name
            )

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity <= 0:
            raise Exception("Quantity must be positive")
        if self.get_promotion() is None:
            return self.price * quantity
        return self.promotion.apply_promotion(self, quantity)


class LimitedProduct(Product):
    """Represent a limited product available in the store."""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Show the product."""
        if self.promotion is None:
            print(
                self.name,
                "Price:", self.price,
                "Quantity:", self.quantity,
                "Maximum:", self.maximum
            )
        else:
            print(
                self.name,
                "Price:", self.price,
                "Quantity:", self.quantity,
                "Promotion:", self.promotion.name,
                "Maximum:", self.maximum
            )

    def buy(self, quantity) -> float:
        """Make the products buy."""
        if quantity > self.maximum:
            raise Exception(f"You can only buy {self.maximum} products")
        return super().buy(quantity)
