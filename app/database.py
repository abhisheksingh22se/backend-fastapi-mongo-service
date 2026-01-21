from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Required environment variables
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME", "hospital")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "patients")

# Error if essential config is missing
if not MONGO_URL:
    raise EnvironmentError("❌ MONGO_URL is not set in the environment or .env file.")

# MongoDB client and collection accessor
client = MongoClient(MONGO_URL)

def get_patient_collection():
    db = client[DB_NAME]
    return db[COLLECTION_NAME]
