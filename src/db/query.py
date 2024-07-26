import os
import sqlite3
from typing import List, Dict, Any

from models.product import Product
from models.product_detail import ProductDetail

DB_PATH = os.path.join(os.path.abspath(os.getcwd()), "db/payterra_test.sqlite")


def query_products() -> List[str]:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT name from products;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return [row[0] for row in rows]


def query_product_details(product_name: str) -> List[Dict[str, Any]]:
    query = """
    SELECT p.name, p.vendor, 
           (SELECT GROUP_CONCAT(st.name) 
            FROM "solution-type" st 
            JOIN "solution-type-graph" stg ON st.solution_type_id = stg.solution_type_id 
            WHERE stg.product_id = p.product_id) AS solution_type, 
           p.description, p.website, 
           pd.type, pd."group", pd.value, pd.description 
    FROM products p 
    JOIN "product-details" pd ON p.product_id = pd.product_id 
    WHERE p.name = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(query, (product_name,))
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    connection.close()

    products_dict = {}
    for row in rows:
        product_data = dict(zip(column_names, row))
        if product_data["name"] not in products_dict:
            products_dict[product_data["name"]] = Product(
                vendor=product_data["vendor"],
                solution_type=product_data["solution_type"],
                description=product_data["description"],
                website=product_data["website"],
                details=[],
            )
        product_detail = ProductDetail(
            type=product_data["type"],
            group=product_data["group"],
            value=product_data["value"],
            description=product_data["description"],
        )
        products_dict[product_data["name"]].details.append(product_detail)

    return products_dict
