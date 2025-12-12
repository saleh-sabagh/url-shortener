"""Business logic for URL shortening operations."""

import random
import string

from app.models.url_model import URL
from app.repositories.url_repository import URLRepository

ALPHABET: str = string.ascii_letters + string.digits
MAX_RETRIES: int = 5


def generate_short_code(length: int = 6) -> str:
    """Generate a random short code.

    Args:
        length: Length of the short code to generate. Defaults to 6.

    Returns:
        A random short code string.
    """
    return "".join(random.choices(ALPHABET, k=length))


class URLService:
    """Service for URL shortening operations."""

    def __init__(self, repository: URLRepository) -> None:
        """Initialize the service with a repository.

        Args:
            repository: URLRepository instance for data operations.
        """
        self.repo = repository

    def create_short_url(self, original_url: str) -> URL:
        """Create a shortened URL.

        Args:
            original_url: The original URL to be shortened.

        Returns:
            The created URL object with generated short code.

        Raises:
            ValueError: If the URL is invalid or missing protocol.
            RuntimeError: If unable to generate a unique short code.
        """
        if not original_url or not original_url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL")

        for _ in range(MAX_RETRIES):
            code = generate_short_code()
            if not self.repo.get_by_short_code(code):
                break
        else:
            raise RuntimeError("Could not generate unique code")

        url_obj = URL(original_url=original_url, short_code=code)
        return self.repo.create(url_obj)
