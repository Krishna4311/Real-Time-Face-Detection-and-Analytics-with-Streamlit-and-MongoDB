from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "Replace this text with MONGODB_URI"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["face_log_db"]
collection = db["detection"]

client.admin.command('ping')
print("Connected!")

