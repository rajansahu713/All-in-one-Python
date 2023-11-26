from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI') 

client = MongoClient(MONGO_URI)

for db_name in client.list_database_names():
    print(db_name)


"""
Documents: basic unit of data in mongoDB
Collection: is a grouping of documents
Database: It is container for collection


Document are json and it store it mongo as BSON it is bit format of json

In MongoDB document are displayed in JSON format, but stored in BSON.

BSON Support additional data types, like dates, numbers, and objectIds

In Mongo objectid  field is use to create create unique identifier in Mongodb 

we can store different type of document structure data in the same collections but also we can make schema oriented in mongo db by declearing validation.

type of data modeling

Relationship types
1. one to one
2. one to many
3. many to many

Ways to model relationships
1. Embedding 
3. Referencing

Data that is accessed together should be stored together.

Embending data:
1. One to many 
2. many to many


difference between Embedding and referening
1. Single query to retrieve data
2. single operation to update/delete data
3. data duplications
4. Large documents

1. No duplication
2. Smaller documents
3. Need to join data from multiple documents

There are two official drive that are use to connect with python
1. Pymongo (for synchronous)
2. Motor (for asynchronous)
"""