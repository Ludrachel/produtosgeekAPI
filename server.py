from fastapi import FastAPI                              # type: ignore
from database.db import sync_database, get_engine
from models.product import ProductCreate, Product
from controllers.products_controllers import router

app = FastAPI()

async def get_db():
    yield sync_database(get_engine())

app.include_router(router, prefix='/products')