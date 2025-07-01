from fastapi import FastAPI

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
