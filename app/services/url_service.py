import random, string
from app.repositories.url_repository import URLRepository
from app.models.url_model import URL

ALPHABET = string.ascii_letters + string.digits

def generate_short_code(length: int = 6) -> str:
    return ''.join(random.choices(ALPHABET, k=length))

class URLService:
    def __init__(self, repository: URLRepository):
        self.repo = repository

    def create_short_url(self, original_url: str) -> URL:
        # validation basic
        if not original_url or not original_url.startswith(("http://","https://")):
            raise ValueError("Invalid URL")

        # try generate unique code with retries
        for _ in range(5):
            code = generate_short_code()
            if not self.repo.get_by_short_code(code):
                break
        else:
            # fallback: use timestamp or raise
            raise RuntimeError("Could not generate unique code")

        url_obj = URL(original_url=original_url, short_code=code)
        return self.repo.create(url_obj)
