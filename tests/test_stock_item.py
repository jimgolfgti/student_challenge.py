import pytest
from student_challenge.price_point import PricePoint
from student_challenge.stock_item import StockItem


@pytest.mark.parametrize(
    "price, quantity, result", [(5, 1, 5), (10, 2, 20), (15, 3, 45)]
)
def test_calculate_price_for_single_item_price_point(
    price: float, quantity: int, result: float
):
    item = StockItem("foo", [PricePoint(price)])
    assert item.calculate_price(quantity) == result


@pytest.mark.parametrize("quantity, result", [(1, 6), (2, 10), (3, 16)])
def test_calculate_price_for_multibuy_item_price_points(quantity: int, result: float):
    price_points = [PricePoint(6), PricePoint(10, 2)]
    item = StockItem("bar", price_points)
    assert item.calculate_price(quantity) == result


def test_stock_item_ensures_at_least_one_price_point():
    with pytest.raises(ValueError) as exinfo:
        StockItem("baz", [])

    assert exinfo.value.args[0] == "Must have at least one PricePoint"


def test_stock_item_ensures_at_least_one_single_item_price_point():
    with pytest.raises(ValueError) as exinfo:
        StockItem("qux", [PricePoint(1, 2)])

    assert exinfo.value.args[0] == "Must have one single item PricePoint"


def test_stock_item_ensures_price_point_quantities_are_unique():
    with pytest.raises(ValueError) as exinfo:
        StockItem("quux", [PricePoint(1), PricePoint(1)])

    assert exinfo.value.args[0] == "Must have unique quantity PricePoints"


def test_calculate_price_quantity_cannot_be_negative():
    item = StockItem("foo", [PricePoint(1)])
    with pytest.raises(ValueError) as exinfo:
        item.calculate_price(-1)

    assert exinfo.value.args[0] == "Quantity must be >= 1"


def test_calculate_price_quantity_cannot_be_zero():
    item = StockItem("foo", [PricePoint(1)])
    with pytest.raises(ValueError) as exinfo:
        item.calculate_price(0)

    assert exinfo.value.args[0] == "Quantity must be >= 1"
