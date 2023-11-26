from pymongo import MongoClient
import os
import datetime

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

new_account=[
    {
    "account_holder":"ravi kumar",
    "account_id":"M789456334",
    "account_type":"saving",
    "balance":7897854,
    "last_updated":datetime.datetime.now()
    },
    {
    "account_holder":"sachin gupta",
    "account_id":"M789456354",
    "account_type":"current",
    "balance":7898564,
    "last_updated":datetime.datetime.now()
    }
]

result = account_collection.insert_many(new_account)

document_id = result.inserted_ids

print("numbser of documents", len(document_id))
print(f"_id od the inserted: {document_id}")