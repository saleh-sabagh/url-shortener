from fastapi import FastAPI
from api.url_router import router as url_router

app = FastAPI()

app.include_router(url_router)
