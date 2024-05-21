from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    friends: List[int] = []

    class Config:
        orm_mode = True
class FriendRequestBase(BaseModel):
    sender_id: int
    receiver_id: int

class FriendRequestCreate(FriendRequestBase):
    pass

class FriendRequest(FriendRequestBase):
    id: int
    status: str  # e.g., "pending", "accepted", "rejected"

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    admin_id: int

    class Config:
        orm_mode = True

class AdvertisementBase(BaseModel):
    content: str

class AdvertisementCreate(AdvertisementBase):
    pass

class Advertisement(AdvertisementBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
