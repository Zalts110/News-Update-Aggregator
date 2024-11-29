from pydantic import BaseModel
from typing import List

class NewsRequest(BaseModel):
    categories: List[str]
    language: str = "en"
    max_articles: int = 5
