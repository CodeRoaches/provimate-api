from fastapi_camelcase import CamelModel
from pydantic.types import UUID


class ProductCreate(CamelModel):
    name: str
    category: str
    unit: str

    class Config:
        from_attributes = True
        
class ProductUpdate(CamelModel):
    name: str
    category: str
    unit: str


class ProductResponse(CamelModel):
    id: UUID
    name: str
    category: str
    unit: str

    class Config:
        from_attributes = True