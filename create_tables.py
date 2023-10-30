from sqlalchemy import create_engine
from database.base import Base  # Importando o 'Base' do seu módulo 'base'

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/posdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)
