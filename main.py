from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/mutual-funds/create", response_model=schemas.MutualFund)
def create_mutual_fund(mutual_fund: schemas.MutualFundCreate, db: Session = Depends(get_db)):
    return crud.create_mutual_fund(db=db, mutual_fund=mutual_fund)

@app.get("/mutual-funds/fetch", response_model=list[schemas.MutualFund])
def read_mutual_funds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mutual_funds = crud.get_mutual_funds(db, skip=skip, limit=limit)
    return mutual_funds

@app.get("/mutual-funds/{mutual_fund_id}", response_model=schemas.MutualFund)
def read_mutual_fund(mutual_fund_id: int, db: Session = Depends(get_db)):
    db_mutual_fund = crud.get_mutual_fund(db, mutual_fund_id=mutual_fund_id)
    if db_mutual_fund is None:
        raise HTTPException(status_code=404, detail="Mutual fund not found")
    return db_mutual_fund

@app.post("/sector-allocations/create", response_model=schemas.SectorAllocation)
def create_sector_allocation(sector_allocation: schemas.SectorAllocationCreate, db: Session = Depends(get_db)):
    return crud.create_sector_allocation(db=db, sector_allocation=sector_allocation)

@app.get("/sector-allocations/{mutual_fund_id}", response_model=list[schemas.SectorAllocation])
def read_sector_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_sector_allocations(db, mutual_fund_id=mutual_fund_id)

@app.post("/stock-allocations/create", response_model=schemas.StockAllocation)
def create_stock_allocation(stock_allocation: schemas.StockAllocationCreate, db: Session = Depends(get_db)):
    return crud.create_stock_allocation(db=db, stock_allocation=stock_allocation)

@app.get("/stock-allocations/{mutual_fund_id}", response_model=list[schemas.StockAllocation])
def read_stock_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_allocations(db, mutual_fund_id=mutual_fund_id)

@app.post("/market-cap-allocations/create", response_model=schemas.MarketCapAllocation)
def create_market_cap_allocation(market_cap_allocation: schemas.MarketCapAllocationCreate, db: Session = Depends(get_db)):
    return crud.create_market_cap_allocation(db=db, market_cap_allocation=market_cap_allocation)

@app.get("/market-cap-allocations/{mutual_fund_id}", response_model=list[schemas.MarketCapAllocation])
def read_market_cap_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_market_cap_allocations(db, mutual_fund_id=mutual_fund_id)