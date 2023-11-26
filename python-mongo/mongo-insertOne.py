from pymongo import MongoClient
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')
print(MONGO_URI)

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

new_account={
    "account_holder":"rajan sahu",
    "account_id":"M789456321",
    "account_type":"checking",
    "balance":7895665,
    "last_updated":datetime.datetime.now()
}

result = account_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id od the inserted: {document_id}")