"""FastAPI application entry point for URL Shortener service."""

from fastapi import FastAPI
from app.api.url_router import router as url_router

app = FastAPI(title="URL Shortener")
app.include_router(url_router)
