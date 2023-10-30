from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database.base import Base
import datetime

class Order(Base):
    __tablename__ = "orders"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, default=0.0)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    items = relationship("Item", back_populates="order")
    owner = relationship("User", back_populates="orders")
