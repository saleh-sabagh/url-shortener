from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    original_url: str
    short_code: str
    created_at: datetime

class ResponseModel(BaseModel):
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None
