import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.query import query_product_details, query_products
from middleware.exception import ExceptionHandlerMiddleware
from models.responses.default_response import DefaultResponse
from models.responses.product_response import ProductResponse
from models.responses.version_response import VersionResponse

load_dotenv()

APP_NAME = os.environ.get("APP_NAME", "CF PAYTERRA")
VERSION = os.environ.get("VERSION", "v1.0.0")

# Setup FastAPI app
app = FastAPI(title=APP_NAME, version=VERSION)

# Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enable Custom Exception Handling Middleware
app.add_middleware(ExceptionHandlerMiddleware)


# Routes
@app.get("/")
def get_index() -> DefaultResponse:
    """
    Responds with a welcome message at the root path of the application.

    This synchronous endpoint is the default route for the application and is
    accessed via a GET request. When invoked, it returns a JSON object with a
    greeting message, indicating that the application is successfully running.

    Returns:
        dict: A JSON object containing a welcome message to CF's RAG Application.

    Example usage:
        curl http://localhost:8000/
    """
    return DefaultResponse()


@app.get("/status")
def get_api_status() -> VersionResponse:
    """
    Retrieves the current version of the API.

    This synchronous endpoint is a quick way to check the API version. It returns a JSON object containing
    the version number. This can be useful for debugging, logging, or ensuring compatibility
    with client applications.

    Returns:
       dict: A JSON object containing the API version number.

    Example usage:
    curl http://localhost:8000/status
    """
    return VersionResponse(version=VERSION)


@app.get("/products")
def get_products() -> ProductResponse:
    """
    Responds with a list of all products in the database with their details.

    This synchronous endpoint is the default route for retrieving all product information.

    Returns:
        dict: A JSON object containing a list of product detail dictionaries.

    Example usage:
        curl http://localhost:8000/products
    """
    products = {}
    product_names = query_products()
    for name in product_names:
        product_details = query_product_details(name)
        products[name] = product_details[name]

    return ProductResponse(products=products)


@app.get("/products/{product_name}")
def get_product_details(product_name: str) -> ProductResponse:
    """
    Responds with a list of the specified product in the database with its details.

    This synchronous endpoint is the default route for retrieving a single product's information.

    Returns:
        dict: A JSON object containing a list of product detail dictionaries.

    Example usage:
        curl http://localhost:8000/products/Exactpay
    """
    return ProductResponse(products=query_product_details(product_name))
