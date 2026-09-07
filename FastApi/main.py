from fastapi import (
    FastAPI,
    HTTPException,
    Header,
    Query,
    Path,
    status,
)

from pydantic import BaseModel, Field
from typing import Optional


# ============================================================
# 2. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="FastAPI Basics Tutorial",
    description="A single-file example covering FastAPI fundamentals.",
    version="1.0.0",
)

# ============================================================
# 3. SIMPLE DATABASE
# ============================================================
# This is NOT a real database.
# We are using a Python dictionary just to demonstrate CRUD.

products = {
    1: {
        "id": 1,
        "name": "Laptop",
        "price": 75000,
        "category": "Electronics",
    },
    2: {
        "id": 2,
        "name": "Mouse",
        "price": 1200,
        "category": "Accessories",
    },
}

# ============================================================
# 4. PYDANTIC MODELS
# ============================================================
# Pydantic models define the structure of incoming/outgoing data.
#
# Example JSON:
#
# {
#     "name": "Keyboard",
#     "price": 2500,
#     "category": "Accessories"
# }

class Product(BaseModel):
    name: str
    price: float
    category: str


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str


class ProductUpdate(BaseModel):
    # Optional fields allow partial updates.
    name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None

# ============================================================
# 5. BASIC GET ROUTE
# ============================================================

@app.get("/")
def home():
    """
    Basic GET request.

    URL:
        GET /

    Response:
        JSON
    """

    return {
        "message": "Welcome to FastAPI!",
        "docs": "/docs",
        "redoc": "/redoc",
    }

# ============================================================
# 6. ANOTHER GET ROUTE
# ============================================================

@app.get("/about")
def about():
    return {
        "application": "FastAPI Basics",
        "language": "Python",
        "framework": "FastAPI",
    }

# ============================================================
# 7. PATH PARAMETERS
# ============================================================
#
# URL:
#     /hello/Soham
#
# "name" comes directly from the URL.


@app.get("/hello/{name}")
def hello_user(name: str):
    return {
        "message": f"Hello, {name}!"
    }

# ============================================================
# 8. PATH PARAMETER WITH INTEGER
# ============================================================

@app.get("/square/{number}")
def square_number(number: int):
    """
    FastAPI automatically converts the URL value to int.

    /square/5

    Result:
        25
    """

    return {
        "number": number,
        "square": number * number,
    }

# ============================================================
# 9. QUERY PARAMETERS
# ============================================================
#
# Query parameters come after ? in the URL.
#
# Example:
#
# /search?keyword=laptop
#
# "keyword" is a query parameter.

@app.get("/search")
def search_product(keyword: str):
    return {
        "search_keyword": keyword
    }


# ============================================================
# 10. OPTIONAL QUERY PARAMETER
# ============================================================

@app.get("/products")
def get_products(
    category: Optional[str] = None,
):
    """
    Example:

        /products

    OR:

        /products?category=Electronics
    """

    result = list(products.values())

    if category:
        result = [
            product
            for product in result
            if product["category"].lower() == category.lower()
        ]

    return {
        "count": len(result),
        "products": result,
    }

# ============================================================
# 11. QUERY PARAMETER VALIDATION
# ============================================================

@app.get("/products/filter")
def filter_products(
    min_price: float = Query(
        0,
        ge=0,
        description="Minimum product price",
    ),
    max_price: float = Query(
        1000000,
        ge=0,
        description="Maximum product price",
    ),
):

    result = [
        product
        for product in products.values()
        if min_price <= product["price"] <= max_price
    ]

    return result



# ============================================================
# 12. PATH PARAMETER VALIDATION
# ============================================================

@app.get("/product/{product_id}")
def get_product(
    product_id: int = Path(
        ...,
        gt=0,
        description="ID of the product",
    )
):
    """
    Example:

        /product/1

    FastAPI checks that product_id:
        - is an integer
        - is greater than 0
    """

    product = products.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

# ============================================================
# 13. POST REQUEST — REQUEST BODY
# ============================================================
#
# POST is normally used to create data.
#
# JSON:
#
# {
#     "name": "Keyboard",
#     "price": 2500,
#     "category": "Accessories"
# }

@app.post("/products")
def create_product(product: Product):

    # Generate a simple ID.
    new_id = max(products.keys(), default=0) + 1

    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
    }

    products[new_id] = new_product

    return {
        "message": "Product created successfully",
        "product": new_product,
    }

# ============================================================
# 14. POST WITH RESPONSE MODEL
# ============================================================

@app.post(
    "/products/validated",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product_with_response_model(
    product: Product,
):

    new_id = max(products.keys(), default=0) + 1

    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
    }

    products[new_id] = new_product

    return new_product


# ============================================================
# 15. PUT REQUEST
# ============================================================
#
# PUT is generally used to replace/update a resource.


@app.put("/products/{product_id}")
def replace_product(
    product_id: int,
    product: Product,
):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    products[product_id] = {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
    }

    return {
        "message": "Product updated",
        "product": products[product_id],
    }


# ============================================================
# 16. PATCH REQUEST
# ============================================================
#
# PATCH is generally used for partial updates.
#
# Example JSON:
#
# {
#     "price": 70000
# }
#
# Only the price will change.


@app.patch("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    existing_product = products[product_id]

    # exclude_unset=True means:
    # only fields actually provided by the user are returned.

    updates = product.model_dump(exclude_unset=True)

    existing_product.update(updates)

    return {
        "message": "Product partially updated",
        "product": existing_product,
    }

# ============================================================
# 17. DELETE REQUEST
# ============================================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted",
        "product": deleted_product,
    }