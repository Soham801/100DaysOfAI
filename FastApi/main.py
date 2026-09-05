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