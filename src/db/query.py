import os
import sqlite3
from fastapi import HTTPException
from typing import List

from models.product import Product
from models.product_detail import ProductDetail

DB_PATH = os.path.join(os.path.abspath(os.getcwd()), "db/payterra_test.sqlite")


def query_products() -> List[str]:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT product_id from products;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return [row[0] for row in rows]


def query_product_details_by_id(product_id: str) -> Product:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT p.product_id, p.name, p.vendor,
           (SELECT GROUP_CONCAT(st.name) 
            FROM "solution-type" st 
            JOIN "solution-type-graph" stg ON st.solution_type_id = stg.solution_type_id 
            WHERE stg.product_id = p.product_id) AS solution_type, 
           p.description, p.website, 
           pd.type, pd."group", pd.value, pd.description 
    FROM products p 
    JOIN "product-details" pd ON p.product_id = pd.product_id
    WHERE p.product_id = ?;
    """

    cursor.execute(query, (product_id,))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    if not rows:
        raise HTTPException(
            status_code=400,
            detail=f"No product found with product_id: {product_id}",
        )

    product_id, name, vendor, solution_type, description, website = rows[0][:6]
    details = [
        ProductDetail(product_id=product_id, type=row[6], group=row[7], value=row[8], description=row[9])
        for row in rows
    ]

    return Product(
        product_id=product_id,
        name=name,
        vendor=vendor,
        solution_type=solution_type,
        description=description,
        website=website,
        details=details,
    )
