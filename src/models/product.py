from pydantic import BaseModel
from typing import List, Optional

from models.product_detail import ProductDetail


class Product(BaseModel):
    vendor: Optional[str] = None
    solution_type: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    details: List[ProductDetail]
