from typing import Dict, Iterator


class Basket:
    def __init__(self) -> None:
        self._contents: Dict[str, int] = {}

    def add_item(self, item: str) -> None:
        quantity = self._contents.setdefault(item, 0) + 1
        self._contents[item] = quantity

    def remove_item(self, item: str) -> None:
        quantity = self._contents.setdefault(item, 1) - 1
        if quantity > 0:
            self._contents[item] = quantity
        else:
            self._contents.pop(item)

    def __iter__(self) -> Iterator[tuple[str, int]]:
        return iter(self._contents.items())
