import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # Load environment variables from .env file
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MongoDB URI not found")

conn = MongoClient(MONGO_URI)
