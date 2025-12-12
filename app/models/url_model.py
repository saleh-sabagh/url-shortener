"""SQLAlchemy models for URL shortener."""

from sqlalchemy import Column, Integer, String, DateTime, func, Boolean

from app.core.db import Base


class URL(Base):
    """URL database model for storing shortened URLs.

    Attributes:
        id: Primary key identifier.
        original_url: The full original URL to be shortened.
        short_code: Unique short code for the URL.
        created_at: Timestamp when the URL was created.
        is_active: Flag indicating if the URL is active.
    """

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(2048), nullable=False)
    short_code = Column(String(16), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
