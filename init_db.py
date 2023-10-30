from database import Base, engine
from app.models.user import User  # E outros modelos que você tenha

Base.metadata.create_all(bind=engine)
