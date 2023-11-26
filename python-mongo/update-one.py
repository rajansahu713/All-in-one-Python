from pymongo import MongoClient
import os
import pprint
from bson.objectid import ObjectId 
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

document_id_update = {"_id":ObjectId("63e8d660e6edbdc2461b9c05")}

add_to_balanace = {"$inc":{"balance":100}}

pprint.pprint(account_collection.find_one(document_id_update))

result = account_collection.update_one(document_id_update, add_to_balanace)

print("Documents updayed:  ",str(result.modified_count))

pprint.pprint(account_collection.find_one(document_id_update))

client.close()
