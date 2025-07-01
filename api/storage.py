"""In-memory storage for the API."""

from typing import Optional

from api.models import Item, ItemCreate


class InMemoryStorage:
    """In-memory storage for items."""

    def __init__(self) -> None:
        """Initialize the storage."""
        self._items: dict[int, Item] = {}
        self._next_id: int = 1

    def create_item(self, item_create: ItemCreate) -> Item:
        """Create a new item."""
        item = Item(id=self._next_id, **item_create.model_dump())
        self._items[item.id] = item
        self._next_id += 1
        return item

    def get_item(self, item_id: int) -> Optional[Item]:
        """Get an item by its ID."""
        return self._items.get(item_id)
