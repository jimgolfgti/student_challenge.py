import pytest
from student_challenge.basket import Basket
from student_challenge.price_point import PricePoint
from student_challenge.stock_item import StockItem
from student_challenge.store import Store


@pytest.fixture
def store():
    return Store(
        [StockItem("table", [PricePoint(50)]), StockItem("chair", [PricePoint(10)])]
    )


def test_store_returns_zeros_with_empty_basket(store: Store):
    assert store.calculate_total_price(Basket()) == {"total": 0, "delivery_charge": 0}


def test_basket_with_unknown_inventory_raises_error(store: Store):
    basket = Basket()
    basket.add_item("sofa")
    with pytest.raises(Exception) as exinfo:
        store.calculate_total_price(basket)

    assert exinfo.value.args[0] == "No inventory pricing found for 'sofa'"


@pytest.mark.parametrize(
    "tables, chairs, expected_total, expected_delivery",
    [(0, 4, 40, 7), (1, 4, 90, 0), (0, 5, 50, 0)],
)
def test_store_returns_expected_totals(
    store: Store,
    tables: int,
    chairs: int,
    expected_total: float,
    expected_delivery: float,
):
    basket = Basket()
    for _ in range(tables):
        basket.add_item("table")
    for _ in range(chairs):
        basket.add_item("chair")

    assert store.calculate_total_price(basket) == {
        "total": expected_total,
        "delivery_charge": expected_delivery,
    }
