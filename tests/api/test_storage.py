from api.models import ItemCreate
from api.storage import InMemoryStorage


def test_create_and_get_item() -> None:
    """Test creating and getting an item."""
    storage = InMemoryStorage()
    item_create = ItemCreate(name="Test Item", price=10.0)

    # Create an item
    created_item = storage.create_item(item_create)
    assert created_item.id == 1
    assert created_item.name == "Test Item"
    assert created_item.price == 10.0
    assert created_item.created_at is not None

    # Get the item
    retrieved_item = storage.get_item(created_item.id)
    assert retrieved_item is not None
    assert retrieved_item.id == created_item.id
    assert retrieved_item.name == created_item.name

    # Get a non-existent item
    non_existent_item = storage.get_item(999)
    assert non_existent_item is None
