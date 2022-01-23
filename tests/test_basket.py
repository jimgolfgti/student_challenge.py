from typing import Mapping
import pytest
from student_challenge.basket import Basket


@pytest.fixture
def basket():
    basket = Basket()
    basket.add_item("foo")
    basket.add_item("bar")
    basket.add_item("foo")
    basket.add_item("baz")
    basket.add_item("foo")
    basket.add_item("bar")
    return basket


def contents(basket: Basket) -> Mapping[str, int]:
    return {k: v for k, v in basket}


def test_add_item_accumulates_totals(basket: Basket):
    assert contents(basket) == {"foo": 3, "bar": 2, "baz": 1}


def test_remove_item_updates_totals(basket: Basket):
    basket.remove_item("bar")
    assert contents(basket) == {"foo": 3, "bar": 1, "baz": 1}


def test_remove_item_clears_zero_counts(basket: Basket):
    basket.remove_item("baz")
    assert contents(basket) == {"foo": 3, "bar": 2}


def test_remove_item_with_missing_item_does_not_raise(basket: Basket):
    basket.remove_item("quux")


def test_basket_is_iterable(basket: Basket):
    assert [quantity for _, quantity in basket] == [3, 2, 1]
