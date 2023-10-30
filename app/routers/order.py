from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.base import SessionLocal, get_db
from app.models.order import Order
from app.models.item import Item
from app.schemas.order import OrderCreateSchema, OrderSchema
from app.schemas.item import ItemCreateSchema, ItemSchema
from app import crud
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/orders/", response_model=List[OrderSchema])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.order.get_all_orders(db=db)
    return orders


@router.post("/")
def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.post("/{order_id}/items/")
def add_item_to_order(order_id: int, item: ItemCreateSchema, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db_item = Item(**item.dict(), order_id=order_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# ... (mais endpoints para outras operações CRUD)
