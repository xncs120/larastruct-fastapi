from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    username: str
    email: str
    password: str
