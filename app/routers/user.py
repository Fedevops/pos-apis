from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from database.base import get_db
from app.utils.password_utils import hash_password

router = APIRouter()

@router.post("/register/")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = User(username=username, hashed_password=hash_password(password))
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully!"}
