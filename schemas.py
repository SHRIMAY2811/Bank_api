from pydantic import BaseModel
from typing import List, Optional

class BankBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BranchBase(BaseModel):
    ifsc: str
    branch: str
    address: str
    city: str
    district: str
    state: str
    bank: BankBase  

    class Config:
        from_attributes = True