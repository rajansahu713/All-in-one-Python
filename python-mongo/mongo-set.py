from pymongo import MongoClient
import os
import datetime
import pprint

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

select_accounts ={"account_type":"saving"}

set_field ={"$set":{"minimum_balance":100}}

result = account_collection.update_many(select_accounts, set_field)

print("Documents matched: ",str(result.matched_count))
print("Documents updated", str(result.modified_count))

pprint.pprint(account_collection.find_one(select_accounts))

client.close()