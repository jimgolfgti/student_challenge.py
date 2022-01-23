import pytest
from student_challenge.price_point import PricePoint


@pytest.mark.parametrize(
    "price, quantity, expected", [(10, 2, 20), (15, 3, 45), (20, 0, 0)]
)
def test_default_price_points(price: float, quantity: int, expected: float):
    assert PricePoint(price).apply(quantity) == (expected, 0)


@pytest.mark.parametrize(
    "discount, items, quantity, expected_total, expected_remainder",
    [(10, 2, 2, 10, 0), (8, 3, 4, 8, 1), (8, 2, 1, 0, 1)],
)
def test_multibuy_price_points(
    discount: float,
    items: int,
    quantity: int,
    expected_total: float,
    expected_remainder: int,
):
    assert PricePoint(discount, items).apply(quantity) == (
        expected_total,
        expected_remainder,
    )


def test_price_point_quantity_cannot_be_negative():
    with pytest.raises(ValueError) as exinfo:
        PricePoint(1, -1)

    assert exinfo.value.args[0] == "Quantity must be >= 1"


def test_price_point_quantity_cannot_be_zero():
    with pytest.raises(ValueError) as exinfo:
        PricePoint(1, 0)

    assert exinfo.value.args[0] == "Quantity must be >= 1"


def test_price_point_price_cannot_be_negative():
    with pytest.raises(ValueError) as exinfo:
        PricePoint(-0.01)

    assert exinfo.value.args[0] == "Price must be >= 0.01"


def test_price_point_price_cannot_be_zero():
    with pytest.raises(ValueError) as exinfo:
        PricePoint(0)

    assert exinfo.value.args[0] == "Price must be >= 0.01"
