from pydantic import BaseModel
from typing import List
from datetime import date

class Portfolio(BaseModel):
    id: str
    name: str
    owner: str
    total_value: int
    positions: List[str]


