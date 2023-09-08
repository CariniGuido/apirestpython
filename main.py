

from fastapi import FastAPI
from app.routes import router as items_router
from app.database import engine  
app = FastAPI()

app.include_router(items_router, prefix="/items", tags=["items"])
