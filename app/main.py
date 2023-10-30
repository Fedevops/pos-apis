from fastapi import FastAPI
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.routers import auth, order, user

# DATABASE_URL = "sqlite:///./test.db"  # Em produção, use um banco de dados mais robusto como PostgreSQL
DATABASE_URL = "postgresql://postgres:1234@localhost/posdb"


engine = create_engine(DATABASE_URL)
# Base = declarative_base()
# Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)



app = FastAPI(
    title="Restaurant POS System",
    description="API for managing orders and items in a restaurant POS system.",
    version="1.0.0",
)

# Inclua os roteadores
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(user.router, prefix="/register", tags=["Users"])

# Evento de inicialização para criar a base de dados (se não existir)
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()