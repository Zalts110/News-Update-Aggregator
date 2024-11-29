from pydantic import BaseModel

class Settings(BaseModel):
    MONGO_URI: str = "mongodb://localhost:27017/news_aggregator"

# Instantiate the settings object
settings = Settings()

