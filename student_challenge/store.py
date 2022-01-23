from typing import Mapping, Sequence
from student_challenge.basket import Basket
from student_challenge.stock_item import StockItem


class Store:
    def __init__(self, inventory: Sequence[StockItem]) -> None:
        self.__inventory = {item.id: item for item in inventory}

    @staticmethod
    def __calculate_delivery_charge(total: float) -> float:
        if total <= 0 or total >= 50:
            return 0.0
        else:
            return 7.0

    def calculate_total_price(self, basket: Basket) -> Mapping[str, float]:
        total = 0.0
        for item, quantity in basket:
            if item not in self.__inventory:
                raise Exception("No inventory pricing found for '%s'" % item)
            total += self.__inventory[item].calculate_price(quantity)

        delivery_charge = self.__calculate_delivery_charge(total)
        return {"total": total, "delivery_charge": delivery_charge}
