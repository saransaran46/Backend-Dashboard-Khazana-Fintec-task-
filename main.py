# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# import crud, models, schemas
# from database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/mutual-funds/create/", response_model=schemas.MutualFund)
# def create_mutual_fund(mutual_fund: schemas.MutualFundCreate, db: Session = Depends(get_db)):
#     return crud.create_mutual_fund(db=db, mutual_fund=mutual_fund)

# @app.get("/mutual-funds/fetch/", response_model=list[schemas.MutualFund])
# def read_mutual_funds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     mutual_funds = crud.get_mutual_funds(db, skip=skip, limit=limit)
#     return mutual_funds

# @app.get("/mutual-funds/{mutual_fund_id}", response_model=schemas.MutualFund)
# def read_mutual_fund(mutual_fund_id: int, db: Session = Depends(get_db)):
#     db_mutual_fund = crud.get_mutual_fund(db, mutual_fund_id=mutual_fund_id)
#     if db_mutual_fund is None:
#         raise HTTPException(status_code=404, detail="Mutual fund not found")
#     return db_mutual_fund

# @app.post("/sector-allocations/create/", response_model=schemas.SectorAllocation)
# def create_sector_allocation(sector_allocation: schemas.SectorAllocationCreate, db: Session = Depends(get_db)):
#     return crud.create_sector_allocation(db=db, sector_allocation=sector_allocation)

# @app.get("/sector-allocations/{mutual_fund_id}", response_model=list[schemas.SectorAllocation])
# def read_sector_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
#     return crud.get_sector_allocations(db, mutual_fund_id=mutual_fund_id)

# @app.post("/stock-allocations/create/", response_model=schemas.StockAllocation)
# def create_stock_allocation(stock_allocation: schemas.StockAllocationCreate, db: Session = Depends(get_db)):
#     return crud.create_stock_allocation(db=db, stock_allocation=stock_allocation)

# @app.get("/stock-allocations/{mutual_fund_id}", response_model=list[schemas.StockAllocation])
# def read_stock_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
#     return crud.get_stock_allocations(db, mutual_fund_id=mutual_fund_id)

# @app.post("/market-cap-allocations/create/", response_model=schemas.MarketCapAllocation)
# def create_market_cap_allocation(market_cap_allocation: schemas.MarketCapAllocationCreate, db: Session = Depends(get_db)):
#     return crud.create_market_cap_allocation(db=db, market_cap_allocation=market_cap_allocation)

# @app.get("/market-cap-allocations/{mutual_fund_id}", response_model=list[schemas.MarketCapAllocation])
# def read_market_cap_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
#     return crud.get_market_cap_allocations(db, mutual_fund_id=mutual_fund_id)







from fastapi import FastAPI, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from typing import Union, Dict, Any

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Endpoint to create a mutual fund (accepts any kind of data)
# @app.post("/mutual-funds/", response_model=schemas.MutualFund)
# def create_mutual_fund(
#     name: str = Form(...),
#     investment_date: str = Form(...),
#     amount_invested: float = Form(...),
#     isin: str = Form(...),
#     nav_at_investment: float = Form(...),
#     returns_since_investment: float = Form(...),
#     db: Session = Depends(get_db)
# ):
#     mutual_fund_data = {
#         "name": name,
#         "investment_date": investment_date,
#         "amount_invested": amount_invested,
#         "isin": isin,
#         "nav_at_investment": nav_at_investment,
#         "returns_since_investment": returns_since_investment,
#     }
#     return crud.create_mutual_fund(db=db, mutual_fund=schemas.MutualFundCreate(**mutual_fund_data))




@app.post("/mutual-funds/", response_model=schemas.MutualFund)
def create_mutual_fund(
    name: str = Form(...),
    investment_date: str = Form(...),
    amount_invested: float = Form(...),
    isin: str = Form(...),
    nav_at_investment: float = Form(...),
    returns_since_investment: float = Form(...),
    db: Session = Depends(get_db)
):
    # Prepare the mutual fund data
    mutual_fund_data = {
        "name": name,
        "investment_date": investment_date,
        "amount_invested": amount_invested,
        "isin": isin,
        "nav_at_investment": nav_at_investment,
        "returns_since_investment": returns_since_investment,
    }
    
    # Call the CRUD function to create the mutual fund
    return crud.create_mutual_fund(db=db, mutual_fund=schemas.MutualFundCreate(**mutual_fund_data))







# Endpoint to fetch mutual funds
@app.get("/mutual-funds/", response_model=list[schemas.MutualFund])
def read_mutual_funds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mutual_funds = crud.get_mutual_funds(db, skip=skip, limit=limit)
    return mutual_funds

# Endpoint to fetch a specific mutual fund by ID
@app.get("/mutual-funds/{mutual_fund_id}", response_model=schemas.MutualFund)
def read_mutual_fund(mutual_fund_id: int, db: Session = Depends(get_db)):
    db_mutual_fund = crud.get_mutual_fund(db, mutual_fund_id=mutual_fund_id)
    if db_mutual_fund is None:
        raise HTTPException(status_code=404, detail="Mutual fund not found")
    return db_mutual_fund

# Endpoint to create a sector allocation (accepts any kind of data)
@app.post("/sector-allocations/", response_model=schemas.SectorAllocation)
def create_sector_allocation(
    mutual_fund_id: int = Form(...),
    sector: str = Form(...),
    allocation_percentage: float = Form(...),
    db: Session = Depends(get_db)
):
    sector_allocation_data = {
        "mutual_fund_id": mutual_fund_id,
        "sector": sector,
        "allocation_percentage": allocation_percentage,
    }
    return crud.create_sector_allocation(db=db, sector_allocation=schemas.SectorAllocationCreate(**sector_allocation_data))

# Endpoint to fetch sector allocations for a mutual fund
@app.get("/sector-allocations/{mutual_fund_id}", response_model=list[schemas.SectorAllocation])
def read_sector_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_sector_allocations(db, mutual_fund_id=mutual_fund_id)

# Endpoint to create a stock allocation (accepts any kind of data)
@app.post("/stock-allocations/", response_model=schemas.StockAllocation)
def create_stock_allocation(
    mutual_fund_id: int = Form(...),
    stock: str = Form(...),
    allocation_percentage: float = Form(...),
    db: Session = Depends(get_db)
):
    stock_allocation_data = {
        "mutual_fund_id": mutual_fund_id,
        "stock": stock,
        "allocation_percentage": allocation_percentage,
    }
    return crud.create_stock_allocation(db=db, stock_allocation=schemas.StockAllocationCreate(**stock_allocation_data))

# Endpoint to fetch stock allocations for a mutual fund
@app.get("/stock-allocations/{mutual_fund_id}", response_model=list[schemas.StockAllocation])
def read_stock_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_allocations(db, mutual_fund_id=mutual_fund_id)

# Endpoint to create a market cap allocation (accepts any kind of data)
@app.post("/market-cap-allocations/", response_model=schemas.MarketCapAllocation)
def create_market_cap_allocation(
    mutual_fund_id: int = Form(...),
    market_cap: str = Form(...),
    allocation_percentage: float = Form(...),
    db: Session = Depends(get_db)
):
    market_cap_allocation_data = {
        "mutual_fund_id": mutual_fund_id,
        "market_cap": market_cap,
        "allocation_percentage": allocation_percentage,
    }
    return crud.create_market_cap_allocation(db=db, market_cap_allocation=schemas.MarketCapAllocationCreate(**market_cap_allocation_data))

# Endpoint to fetch market cap allocations for a mutual fund
@app.get("/market-cap-allocations/{mutual_fund_id}", response_model=list[schemas.MarketCapAllocation])
def read_market_cap_allocations(mutual_fund_id: int, db: Session = Depends(get_db)):
    return crud.get_market_cap_allocations(db, mutual_fund_id=mutual_fund_id)