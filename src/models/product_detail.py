from pydantic import BaseModel
from typing import Optional

from models.product_type import ProductType


class ProductDetail(BaseModel):
    type: ProductType
    group: Optional[str] = None
    value: Optional[str] = None
    description: Optional[str] = None
