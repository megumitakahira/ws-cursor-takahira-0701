from fastapi import FastAPI

app = FastAPI(
    title="Cusor Workshop API",
    description="Sample API for Cursor Workshop",
    version="0.1.0",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Returns the health of the API."""
    return {"status": "ok"}
