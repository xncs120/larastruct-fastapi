from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.config import settings
from core.orm import Orm
from schemas.auth_schema import Token
from schemas.user_schema import UserRequest
from helpers.auth_helper import get_password_hash, authenticate_user, create_access_token

router = APIRouter()

@router.post('/register')
def register_user(user: UserRequest):
    exist_user = Orm('User').orWhere({'username': user.username}).orWhere({'email': user.email}).first()
    if exist_user:
        conflicting_field = 'Username' if exist_user.username == user.username else 'Email'
        raise HTTPException(status_code=400, detail=f'{conflicting_field} already exist')

    hashed_password = get_password_hash(user.password)
    Orm('User').create({
        'name': user.name,
        'username': user.username,
        'email': user.email,
        'password': hashed_password,
        'status': True
    })
    return {'status': 'success', 'message': f'Username [{user.username}] registered successfully.'}

@router.post('/token', response_model=Token)
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}
