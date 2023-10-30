from sqlalchemy.orm import Session
from app.models import order as order_model

def get_all_orders(db: Session):
    return db.query(order_model.Order).all()

def get_order(db: Session, order_id: int):
    return db.query(order_model.Order).filter(order_model.Order.id == order_id).one_or_none()

# ... e assim por diante para outras operações CRUD.
