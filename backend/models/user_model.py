from pydantic import BaseModel, EmailStr
from typing import Optional, List

# User metadata (JWT, prefs)
class UserPreferences(BaseModel):
    theme: str = "dark"
    notifications_enabled: bool = True
    default_calendar_id: str = "primary"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str
    preferences: UserPreferences = UserPreferences()
    is_active: bool = True

    class Config:
        from_attributes = True
