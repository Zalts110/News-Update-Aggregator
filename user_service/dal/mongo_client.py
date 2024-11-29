import os
from pymongo import MongoClient
from config.settings import settings
import logging

logger= logging.getLogger(__name__)

# Get the Mongo URI from environment variable or fallback to settings
mongo_uri = os.getenv('MONGO_URI', settings.MONGO_URI)

logger.fatal(f'mongo URI: {mongo_uri}')

# Create a MongoDB client
try:
    mongo_client = MongoClient(mongo_uri)
    print("MongoDB connected successfully!")
except Exception as e:
    print(f"Failed to connect to db: {e}")

# Access the database
db = mongo_client['news_aggregator']

# Collections
users_collection = db['users']
preferences_collection = db['preferences']
