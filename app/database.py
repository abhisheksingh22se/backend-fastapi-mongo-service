import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# Get Env Vars
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:password@mongodb:27017/")
DB_NAME = os.getenv("DB_NAME", "hospital")

# Create Async Client 
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

def get_collection(collection_name: str):
    return db[collection_name]