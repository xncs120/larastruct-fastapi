from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password: str = Field(nullable=False)
    status: bool = Field(default=True)
