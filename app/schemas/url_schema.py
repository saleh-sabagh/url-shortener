"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, ConfigDict


class URLCreate(BaseModel):
    """Schema for creating a shortened URL.

    Attributes:
        original_url: The original URL to be shortened.
    """

    original_url: HttpUrl


class URLOut(BaseModel):
    """Schema for URL response output.

    Attributes:
        id: Unique identifier.
        original_url: The original URL.
        short_code: The generated short code.
        created_at: Timestamp of creation.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    original_url: str
    short_code: str
    created_at: datetime


class ResponseModel(BaseModel):
    """Generic API response schema.

    Attributes:
        status: Response status (success/failure).
        data: Optional response data.
        message: Optional response message.
    """

    status: str
    data: Optional[dict] = None
    message: Optional[str] = None
