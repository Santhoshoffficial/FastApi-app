from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.role import Role


# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    profile_img: Optional[str] = None


# Create schema (what client sends for registration)
class UserCreate(UserBase):
    password: str   # raw password (will be hashed in service)


# Update schema (PATCH/PUT)
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    profile_img: Optional[str] = None
    user_role_id: Optional[int] = None


# Response schema (what API returns)
class UserInDBBase(UserBase):
    id: int
    user_role_id: int
    role: Optional[Role] = None   # nested Role response

    class Config:
        orm_mode = True


# Final response schema
class User(UserInDBBase):
    pass


# Internal schema (includes hashed_password)
class UserInDB(UserInDBBase):
    hashed_password: str
