import pytest
from httpx import ASGITransport, AsyncClient

from api.main import app


@pytest.mark.anyio
async def test_health_check() -> None:
    """Healtcheck endpoint returns 200."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_create_item() -> None:
    """Create item returns 201."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/items", json={"name": "Test Item", "price": 10.0})
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Item"
        assert data["price"] == 10.0
        assert "id" in data
        assert "created_at" in data


@pytest.mark.anyio
async def test_get_item() -> None:
    """Get item returns 200."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # First, create an item to retrieve
        create_response = await client.post("/items", json={"name": "Test Item 2", "price": 20.0})
        assert create_response.status_code == 201
        item_id = create_response.json()["id"]

        # Now, get the item
        get_response = await client.get(f"/items/{item_id}")
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["id"] == item_id
        assert data["name"] == "Test Item 2"
        assert data["price"] == 20.0


@pytest.mark.anyio
async def test_get_item_not_found() -> None:
    """Get item with non-existent id returns 404."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/items/999")
        assert response.status_code == 404
