class PricePoint:
    def __init__(self, price: float, quantity: int = 1) -> None:
        self._price = price
        self._quantity = quantity
        self.__validate()

    def __validate(self):
        if self._price <= 0.01:
            raise ValueError("Price must be >= 0.01")
        if self._quantity < 1:
            raise ValueError("Quantity must be >= 1")

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def apply(self, quantity: int) -> tuple[float, int]:
        total = quantity // self.quantity * self.price
        return (total, quantity % self.quantity)
