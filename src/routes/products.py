from typing import List, Optional

from db.query import query_products, query_product_details_by_id
from models.product import Product


def get_filtered_products(product_id: Optional[str] = None) -> List[Product]:
    products: List[Product] = []
    product_ids = query_products() if product_id is None else [product_id]

    for id in product_ids:
        product = query_product_details_by_id(id)
        products.append(product)

    return products
