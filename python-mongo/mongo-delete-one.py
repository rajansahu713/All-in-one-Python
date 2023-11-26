from pymongo import MongoClient
import os
import datetime
import pprint
from bson.objectid import ObjectId 

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
print(client)

db = client.bank

account_collection = db.details

document_to_delete ={"_id":ObjectId("63e8d660e6edbdc2461b9c05")}

print("Searching for target")
pprint.pprint(account_collection.find_one(document_to_delete))


result = account_collection.delete_one(document_to_delete)

print("after deleting ")

pprint.pprint(account_collection.find_one(document_to_delete))

print("Documents delete: ",str(result.deleted_count))



client.close()