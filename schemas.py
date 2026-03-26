from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
