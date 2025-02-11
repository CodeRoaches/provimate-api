from uuid import UUID

from api.app import crud
from ..models.products_model import Product

from ..schemas import product_schema as schemas
from ..db.database import get_db
from sqlalchemy.orm.session import Session
from fastapi import Depends, APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("")
def get_products(db: Session = Depends(get_db),):
    products = crud.product.get_multi(db=db)
    return products

@router.get("/{id}")
def get_product(
        id: UUID,
        db: Session = Depends(get_db)
):
    product = crud.product.get_by_id(db=db,id=id)
    if product is None:
        return "dupa"
    return product

@router.post("")
def create_product(
        product: schemas.ProductCreate,
        db: Session = Depends(get_db)
):
    return crud.product.create(db=db, obj_in=product)