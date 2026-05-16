from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

#mongo hirarchy
# Client
#     ↓
# Database
#     ↓
# Collections
#     ↓
# Documents

MONGO_URI=os.getenv('MONGO_URI')
client=MongoClient(MONGO_URI)
db=client['mini_stack_overflow']
users_collection=db['users']

print("MongoDB Connected Successfully")