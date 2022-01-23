from operator import attrgetter
from typing import Sequence
from student_challenge.price_point import PricePoint


class StockItem:
    def __init__(self, id: str, prices: Sequence[PricePoint]) -> None:
        self._id = id
        self._prices = sorted(prices, key=attrgetter("quantity"), reverse=True)
        self.__validate()

    def __validate(self):
        if len(self._prices) == 0:
            raise ValueError("Must have at least one PricePoint")
        if self._prices[-1].quantity != 1:
            raise ValueError("Must have one single item PricePoint")
        last = self._prices[0].quantity
        for price in self._prices[1:]:
            if price.quantity == last:
                raise ValueError("Must have unique quantity PricePoints")
            last = price.quantity

    @property
    def id(self):
        return self._id

    def calculate_price(self, quantity: int) -> float:
        if quantity < 1:
            raise ValueError("Quantity must be >= 1")

        total = 0.0
        for price in self._prices:
            price_total, quantity = price.apply(quantity)
            total += price_total

        return total
