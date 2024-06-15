from fastapi import APIRouter, Depends, HTTPException

from core.orm import Orm
from middlewares.oauth_middleware import auth_user

router = APIRouter()

@router.get('/get/{username}')
def get_user(username: str, auth_user = Depends(auth_user)):
    user = Orm('User').select(['username', 'email', 'name']).where({'username': username}).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.post('/edit')
def edit_user(name: str, auth_user = Depends(auth_user)):
    user = Orm('User').where({'username': auth_user.username}).update({'name': name})
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user
