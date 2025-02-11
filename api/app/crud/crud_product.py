from typing import Optional

from sqlalchemy.orm import Session

from uuid import UUID

from api.app.crud.base import CRUDBase
from api.app.models.products_model import Product
from api.app.schemas.product_schema import ProductUpdate, ProductResponse


class CRUDProduct(CRUDBase[Product, ProductUpdate, ProductResponse]):
    def get_by_id(self, db: Session, *, id: UUID) -> Optional[Product]:
        return (
            db.query(Product).filter(Product.id == id)
        ).first()

    def get_by_name(self, db: Session, *, name: str) -> Optional[Product]:
        return (
            db.query(Product).filter(Product.name == name)
        )


product = CRUDProduct(Product)