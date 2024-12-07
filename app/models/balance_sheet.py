
from pydantic import BaseModel
from typing import List

class Row(BaseModel):
    title: str
    value: float

class BalanceSheet(BaseModel):
    rows: List[Row]
