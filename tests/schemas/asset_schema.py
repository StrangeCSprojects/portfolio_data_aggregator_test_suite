from pydantic import BaseModel
from datetime import date

class Asset(BaseModel):
    symbol: str
    last_price: float
    date: date
    exchange: str
