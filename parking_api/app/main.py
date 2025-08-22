from fastapi import FastAPI
from .routers import vehicles
from .database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)  # Cria tabelas
app.include_router(vehicles.router)
