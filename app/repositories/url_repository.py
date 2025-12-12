from sqlalchemy.ext.asyncio import AsyncSession  # if using async; else normal Session
from sqlalchemy.orm import Session
from app.models.url_model import URL

class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, url_obj: URL):
        self.db.add(url_obj)
        self.db.commit()
        self.db.refresh(url_obj)
        return url_obj

    def get_by_short_code(self, code: str):
        return self.db.query(URL).filter(URL.short_code == code, URL.is_active == True).first()

    def get_all(self):
        return self.db.query(URL).filter(URL.is_active == True).order_by(URL.created_at.desc()).all()

    def delete_by_short_code(self, code: str):
        obj = self.get_by_short_code(code)
        if not obj:
            return None
        self.db.delete(obj)
        self.db.commit()
        return obj
