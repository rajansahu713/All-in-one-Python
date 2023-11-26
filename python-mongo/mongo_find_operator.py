from pymongo import MongoClient
import os
import pprint
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)


db = client.bank

account_collection = db.details

document_id_find={"balance": {"$gt" : 6666}}



cursor = account_collection.find(document_id_find)

num_docs=0
for document in cursor:
    num_docs +=1
    pprint.pprint(document)
    # print(document)
    print()

print("fetch records:  ", num_docs)
