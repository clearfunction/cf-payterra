from pydantic import BaseModel
from typing import List

from models.product import Product


class ProductResponse(BaseModel):
    products: List[Product]
