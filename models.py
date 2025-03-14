from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MutualFund(Base):
    __tablename__ = "mutual_funds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    investment_date = Column(Date)
    amount_invested = Column(Float)
    isin = Column(String, unique=True)
    nav_at_investment = Column(Float)
    returns_since_investment = Column(Float)

    sector_allocations = relationship("SectorAllocation", back_populates="mutual_fund")
    stock_allocations = relationship("StockAllocation", back_populates="mutual_fund")
    market_cap_allocations = relationship("MarketCapAllocation", back_populates="mutual_fund")

class SectorAllocation(Base):
    __tablename__ = "sector_allocation"

    id = Column(Integer, primary_key=True, index=True)
    mutual_fund_id = Column(Integer, ForeignKey("mutual_funds.id"))
    sector = Column(String)
    allocation_percentage = Column(Float)

    mutual_fund = relationship("MutualFund", back_populates="sector_allocations")

class StockAllocation(Base):
    __tablename__ = "stock_allocation"

    id = Column(Integer, primary_key=True, index=True)
    mutual_fund_id = Column(Integer, ForeignKey("mutual_funds.id"))
    stock = Column(String)
    allocation_percentage = Column(Float)

    mutual_fund = relationship("MutualFund", back_populates="stock_allocations")

class MarketCapAllocation(Base):
    __tablename__ = "market_cap_allocation"

    id = Column(Integer, primary_key=True, index=True)
    mutual_fund_id = Column(Integer, ForeignKey("mutual_funds.id"))
    market_cap = Column(String)
    allocation_percentage = Column(Float)

    mutual_fund = relationship("MutualFund", back_populates="market_cap_allocations")