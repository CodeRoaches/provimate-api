from fastapi import FastAPI
from api.app.db.database import Base, engine
from api.app.models.products_model import Product

from api.app.api import product
app = FastAPI()

origins = ["*"]

Base.metadata.create_all(bind=engine)


app.include_router(product.router)

