from pydantic import BaseModel
from datetime import date

class MutualFundBase(BaseModel):
    name: str
    investment_date: date
    amount_invested: float
    isin: str
    nav_at_investment: float
    returns_since_investment: float

class MutualFundCreate(MutualFundBase):
    pass

class MutualFund(MutualFundBase):
    id: int

    class Config:
        orm_mode = True

class SectorAllocationBase(BaseModel):
    mutual_fund_id: int
    sector: str
    allocation_percentage: float

class SectorAllocationCreate(SectorAllocationBase):
    pass

class SectorAllocation(SectorAllocationBase):
    id: int

    class Config:
        orm_mode = True

class StockAllocationBase(BaseModel):
    mutual_fund_id: int
    stock: str
    allocation_percentage: float

class StockAllocationCreate(StockAllocationBase):
    pass

class StockAllocation(StockAllocationBase):
    id: int

    class Config:
        orm_mode = True

class MarketCapAllocationBase(BaseModel):
    mutual_fund_id: int
    market_cap: str
    allocation_percentage: float

class MarketCapAllocationCreate(MarketCapAllocationBase):
    pass

class MarketCapAllocation(MarketCapAllocationBase):
    id: int

    class Config:
        orm_mode = True