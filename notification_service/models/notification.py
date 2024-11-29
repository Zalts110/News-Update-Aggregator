from pydantic import BaseModel,EmailStr
from typing import List

class MessageItem(BaseModel):
    title: str
    url: str

class NotificationRequest(BaseModel):
    recipients:List[EmailStr]
    subject:str
    message:List[MessageItem]
    