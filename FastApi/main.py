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