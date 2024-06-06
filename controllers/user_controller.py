from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from core.database import get_session
from sqlmodel import Session, select
from models.user_model import User
from middlewares.oauth_middleware import get_current_user

router = APIRouter()

@router.get("/{username}")
def get_user(username: str, db: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    statement = select(User.name, User.username, User.email).where(User.username == username)
    user = db.exec(statement).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user._asdict()
