from pydantic import BaseModel,ValidationError,HttpUrl

class Article(BaseModel):
    title:str
    url:HttpUrl
    
