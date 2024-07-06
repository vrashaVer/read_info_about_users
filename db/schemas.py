from pydantic import BaseModel
from pydantic import BaseModel,EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    

class User(UserBase):
    id : int
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass