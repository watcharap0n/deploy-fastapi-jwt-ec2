from app.db import PyObjectId
from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserInfo(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str
    company: Optional[str] = None
    tel: Optional[int] = None
    email: EmailStr

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'name': 'kane',
                'company': 'mango consultant',
                'tel': 941499661,
                'email': 'wera.watcharapon@gmail.com',
            }
        }


class UpdateUserInfo(BaseModel):
    name: str
    company: Optional[str] = None
    tel: Optional[int] = None
    email: EmailStr

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'name': 'kane weera',
                'company': 'thaicom',
                'tel': 941499661,
                'email': 'wera.watcharapon@gmal.com'
            }
        }

