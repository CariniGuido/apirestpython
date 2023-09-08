

from fastapi import FastAPI
from app.routes import router as items_router
from app.database import engine  # Importa el motor de la base de datos desde database.py

app = FastAPI()

app.include_router(items_router, prefix="/items", tags=["items"])
