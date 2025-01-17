from pydantic import BaseModel, Field
from typing import Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="Engineer")
    top_k: Optional[int] = Field(5, example=5, description="Number of top contexts to retrieve (optional)")
