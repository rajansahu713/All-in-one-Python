from pymongo import MongoClient
import os
import datetime
from bson.objectid import ObjectId 

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
print(client)

db = client.bank

account_collection = db.details

document_id={
    "_id":ObjectId("63e8d9d263cf29f9648ce9a4")}



result = account_collection.find_one(document_id)


print("fetch records:  ", result)