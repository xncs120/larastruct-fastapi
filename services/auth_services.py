from datetime import datetime
from jose import jwt
from passlib.context import CryptContext
from core.config import settings
from core.orm import Orm

crypt_schemes = ['bcrypt']

class AuthService:
    def __init__(self, orm_class=Orm):
        self.orm_class = orm_class

    @staticmethod
    def get_password_hash(password: str) -> str:
        return CryptContext(schemes=crypt_schemes, deprecated='auto').hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return CryptContext(schemes=crypt_schemes, deprecated='auto').verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict, expires_at: datetime) -> str:
        to_encode = data.copy()
        to_encode.update({'exp': expires_at})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    
    def authenticate_user(self, username: str, password: str):
        user = self.orm_class('User').where({'username': username}).first()
        if not user:
            return None
        if not self.verify_password(password, user.password):
            return None
        return user