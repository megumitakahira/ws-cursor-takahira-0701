"""Pydantic models for the API."""

from datetime import datetime

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """Model for creating an item."""

    name: str = Field(..., min_length=1, description="Item name")
    price: float = Field(..., gt=0, description="Item price")


class Item(ItemCreate):
    """Model for an item."""

    id: int = Field(..., description="Item ID")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
