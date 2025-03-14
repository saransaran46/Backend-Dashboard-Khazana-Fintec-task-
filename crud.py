from sqlalchemy.orm import Session
import models
import schemas

def get_mutual_fund(db: Session, mutual_fund_id: int):
    return db.query(models.MutualFund).filter(models.MutualFund.id == mutual_fund_id).first()

def get_mutual_funds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MutualFund).offset(skip).limit(limit).all()

def create_mutual_fund(db: Session, mutual_fund: schemas.MutualFundCreate):
    db_mutual_fund = models.MutualFund(**mutual_fund.dict())
    db.add(db_mutual_fund)
    db.commit()
    db.refresh(db_mutual_fund)
    return db_mutual_fund

def get_sector_allocations(db: Session, mutual_fund_id: int):
    return db.query(models.SectorAllocation).filter(models.SectorAllocation.mutual_fund_id == mutual_fund_id).all()

def create_sector_allocation(db: Session, sector_allocation: schemas.SectorAllocationCreate):
    db_sector_allocation = models.SectorAllocation(**sector_allocation.dict())
    db.add(db_sector_allocation)
    db.commit()
    db.refresh(db_sector_allocation)
    return db_sector_allocation

def get_stock_allocations(db: Session, mutual_fund_id: int):
    return db.query(models.StockAllocation).filter(models.StockAllocation.mutual_fund_id == mutual_fund_id).all()

def create_stock_allocation(db: Session, stock_allocation: schemas.StockAllocationCreate):
    db_stock_allocation = models.StockAllocation(**stock_allocation.dict())
    db.add(db_stock_allocation)
    db.commit()
    db.refresh(db_stock_allocation)
    return db_stock_allocation

def get_market_cap_allocations(db: Session, mutual_fund_id: int):
    return db.query(models.MarketCapAllocation).filter(models.MarketCapAllocation.mutual_fund_id == mutual_fund_id).all()

def create_market_cap_allocation(db: Session, market_cap_allocation: schemas.MarketCapAllocationCreate):
    db_market_cap_allocation = models.MarketCapAllocation(**market_cap_allocation.dict())
    db.add(db_market_cap_allocation)
    db.commit()
    db.refresh(db_market_cap_allocation)
    return db_market_cap_allocation