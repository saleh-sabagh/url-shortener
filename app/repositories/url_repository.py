"""Repository layer for URL database operations."""

from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.url_model import URL


class URLRepository:
    """Repository for managing URL database operations."""

    def __init__(self, db: Session) -> None:
        """Initialize the repository with a database session.

        Args:
            db: SQLAlchemy database session.
        """
        self.db = db

    def create(self, url_obj: URL) -> URL:
        """Create and persist a new URL record.

        Args:
            url_obj: URL object to create.

        Returns:
            The created URL object with ID.
        """
        self.db.add(url_obj)
        self.db.commit()
        self.db.refresh(url_obj)
        return url_obj

    def get_by_short_code(self, code: str) -> Optional[URL]:
        """Retrieve a URL by its short code.

        Args:
            code: The short code to search for.

        Returns:
            The URL object if found and active, None otherwise.
        """
        return self.db.query(URL).filter(URL.short_code == code, URL.is_active is True).first()

    def get_all(self) -> List[URL]:
        """Retrieve all active URLs ordered by creation date.

        Returns:
            List of active URL objects ordered by newest first.
        """
        return self.db.query(URL).filter(URL.is_active is True).order_by(URL.created_at.desc()).all()

    def delete_by_short_code(self, code: str) -> Optional[URL]:
        """Delete a URL by its short code.

        Args:
            code: The short code of the URL to delete.

        Returns:
            The deleted URL object if found, None otherwise.
        """
        obj = self.get_by_short_code(code)
        if not obj:
            return None
        self.db.delete(obj)
        self.db.commit()
        return obj
