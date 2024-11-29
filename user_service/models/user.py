from pydantic import BaseModel,EmailStr,ValidationError

class User(BaseModel):
    user_id:str
    name:str
    email:EmailStr
    
    