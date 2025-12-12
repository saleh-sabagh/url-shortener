from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLOut(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime
    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None
