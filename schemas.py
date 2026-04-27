from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    question: str
    session_id: Optional[str] = None