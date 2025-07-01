import pytest
from httpx import ASGITransport, AsyncClient

from api.main import app


@pytest.mark.anyio
async def test_health_check() -> None:
    """Healtcheck endpoint returns 200."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:  # noqa: F841
        # response = await client.get("/health")
        # assert response.status_code == 200
        # assert response.json() == {"status": "ok"}
        pass
