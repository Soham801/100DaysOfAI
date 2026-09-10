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

# ============================================================
# 18. HTTP STATUS CODES
# ============================================================
#
# Common status codes:
#
# 200 -> OK
# 201 -> Created
# 204 -> No Content
# 400 -> Bad Request
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Not Found
# 422 -> Validation Error
# 500 -> Internal Server Error


@app.post(
    "/demo-status",
    status_code=status.HTTP_201_CREATED,
)
def status_code_example():

    return {
        "message": "This endpoint returns HTTP 201 Created"
    }



# ============================================================
# 19. HTTP EXCEPTION
# ============================================================

@app.get("/error-example")
def error_example():

    raise HTTPException(
        status_code=400,
        detail="This is an example error.",
    )

# ============================================================
# 20. REQUEST HEADERS
# ============================================================
#
# Headers are metadata sent with HTTP requests.
#
# Example:
#
# User-Agent
# Authorization
# Content-Type


@app.get("/headers")
def read_headers(
    user_agent: Optional[str] = Header(None),
):

    return {
        "user_agent": user_agent
    }


# ============================================================
# 21. MULTIPLE PARAMETERS TOGETHER
# ============================================================

@app.get("/users/{user_id}/orders")
def get_user_orders(
    user_id: int,
    limit: int = Query(10, ge=1, le=100),
):

    return {
        "user_id": user_id,
        "limit": limit,
        "message": "Example combining path and query parameters",
    }

# ============================================================
# 22. PYDANTIC VALIDATION
# ============================================================

class User(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
    )

    email: str


@app.post("/users")
def create_user(user: User):

    return {
        "message": "User accepted",
        "user": user,
    }



# ============================================================
# 23. RESPONSE MODEL
# ============================================================

class UserResponse(BaseModel):
    name: str
    age: int
    email: str


@app.get(
    "/user-example",
    response_model=UserResponse,
)
def user_example():

    return {
        "name": "Soham",
        "age": 21,
        "email": "soham@example.com",

        # This extra field will NOT appear in the response
        # because it isn't defined in UserResponse.
        "password": "secret",
    }


# ============================================================
# 24. MULTIPLE RESPONSE STATUS CODES
# ============================================================

@app.get(
    "/status-demo/{product_id}",
    response_model=ProductResponse,
)
def status_demo(product_id: int):

    product = products.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product

# ============================================================
# 25. ASYNC ENDPOINT
# ============================================================
#
# FastAPI supports both:
#
# def
#
# and:
#
# async def
#
# async is useful when working with asynchronous I/O,
# such as databases, HTTP requests, files, etc.


@app.get("/async-example")
async def async_example():

    return {
        "message": "This is an asynchronous endpoint."
    }

# ============================================================
# 26. ROUTE WITH MULTIPLE QUERY PARAMETERS
# ============================================================

@app.get("/calculate")
def calculate(
    a: float,
    b: float,
    operation: str = "add",
):

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":

        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero",
            )

        result = a / b

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation",
        )

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result,
    }

# ============================================================
# 27. ROOT HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "FastAPI",
    }

# ============================================================
# 28. APPLICATION ENTRY POINT
# ============================================================
#
# You normally start this application using:
#
#     uvicorn main:app --reload
#
# This section also allows:
#
#     python main.py
#
# to start the server directly.


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )