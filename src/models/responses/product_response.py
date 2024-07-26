from pydantic import BaseModel
from typing import Dict

from models.product import Product


class ProductResponse(BaseModel):
    products: Dict[str, Product]
