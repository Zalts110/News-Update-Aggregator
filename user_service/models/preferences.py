from pydantic import BaseModel,ValidationError
from typing import List

class Preferences(BaseModel):
    user_id: str
    categories:List[str] = []
    delivery_channel:str = "email"
    
