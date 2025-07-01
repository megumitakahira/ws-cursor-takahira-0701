from fastapi import FastAPI, HTTPException

from api.models import Item, ItemCreate
from api.storage import InMemoryStorage

app = FastAPI(
    title="Cusor Workshop API",
    description="Sample API for Cursor Workshop",
    version="0.1.0",
)

storage = InMemoryStorage()


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Returns the health of the API."""
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=201)
async def create_item(item_create: ItemCreate) -> Item:
    """Creates a new item."""
    return storage.create_item(item_create)


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    """Gets an item by its ID."""
    item = storage.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
