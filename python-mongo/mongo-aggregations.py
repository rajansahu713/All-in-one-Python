from pymongo import MongoClient
import os
import pprint
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
print(client)

db = client.bank

account_collection = db.details


select_by_balance ={"$match":{"balance":{"$gt":1000}}}

separate_by_account_calculate_avg_balance={
    "$group":{"_id":"$account_type", "avg_balance":{"$avg":"$balance"}}
}

pipeline=[
    select_by_balance,
    separate_by_account_calculate_avg_balance
]

results = account_collection.aggregate(pipeline)

print()

print("Average balance of checking")

for item in results:
    pprint.pprint(item)

client.close()
