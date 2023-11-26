from pymongo import MongoClient
import os
import pprint

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

document_to_delete ={"balance":{"$lt":2000}}

print("Searching for target")
pprint.pprint(account_collection.find_one(document_to_delete))


result = account_collection.delete_many(document_to_delete)

print("after deleting ")

pprint.pprint(account_collection.find_one(document_to_delete))

print("Documents delete: ",str(result.deleted_count))



client.close()