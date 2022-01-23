"""
  Documentation for Student Challenge.

## Examples
>>> example_usage("")
{'total': 0.0, 'delivery_charge': 0.0}
>>> example_usage("A")
{'total': 8.0, 'delivery_charge': 7.0}
>>> example_usage("B")
{'total': 12.0, 'delivery_charge': 7.0}
>>> example_usage("C")
{'total': 4.0, 'delivery_charge': 7.0}
>>> example_usage("D")
{'total': 7.0, 'delivery_charge': 7.0}
>>> example_usage("E")
{'total': 5.0, 'delivery_charge': 7.0}
>>> example_usage("BB")
{'total': 20.0, 'delivery_charge': 7.0}
>>> example_usage("BBB")
{'total': 32.0, 'delivery_charge': 7.0}
>>> example_usage("BBBB")
{'total': 40.0, 'delivery_charge': 7.0}
>>> example_usage("CCC")
{'total': 10.0, 'delivery_charge': 7.0}
>>> example_usage("CCCC")
{'total': 14.0, 'delivery_charge': 7.0}
>>> example_usage("DD")
{'total': 7.0, 'delivery_charge': 7.0}
>>> example_usage("DDD")
{'total': 14.0, 'delivery_charge': 7.0}
>>> example_usage("EE")
{'total': 10.0, 'delivery_charge': 7.0}
>>> example_usage("EEE")
{'total': 10.0, 'delivery_charge': 7.0}
>>> example_usage("EEEE")
{'total': 15.0, 'delivery_charge': 7.0}
>>> example_usage("DDDDDDDDDDDDDD")
{'total': 49.0, 'delivery_charge': 7.0}
>>> example_usage("BBBBCCC")
{'total': 50.0, 'delivery_charge': 0.0}
>>> example_usage("ABBCCCDDEE")
{'total': 55.0, 'delivery_charge': 0.0}
>>> example_usage("EDCBAEDCBC")
{'total': 55.0, 'delivery_charge': 0.0}
"""


from typing import Mapping
from student_challenge.basket import Basket
from student_challenge.price_point import PricePoint
from student_challenge.stock_item import StockItem
from student_challenge.store import Store


def example_usage(example: str) -> Mapping[str, float]:
    store = Store(
        [
            StockItem("A", [PricePoint(8.0)]),
            StockItem("B", [PricePoint(20.0, 2), PricePoint(12.0)]),
            StockItem("C", [PricePoint(10.0, 3), PricePoint(4.0)]),
            StockItem("D", [PricePoint(7.0, 2), PricePoint(7.0)]),
            StockItem("E", [PricePoint(10.0, 3), PricePoint(5.0)]),
        ]
    )
    basket = Basket()
    for item in example:
        basket.add_item(item)
    return store.calculate_total_price(basket)
