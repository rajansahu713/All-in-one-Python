If not specified 

How to find the data in collection

2. db.collection_name.findOne({_id: ObjectId("66ygdhjvgvjf44435sbhfsh324b")})

1. db.zips.find({ _id: ObjectId("5c8eccc1caa187d17ca6ed16") })

2. db.zips.find({ city: { $in: ["PHOENIX", "CHICAGO"] } })


Opertors

1. db.sales.find({ "items.price": { $gt: 50}})
2. db.sales.find({ "items.price": { $lt: 50}})
db.sales.find({ "customer.age": { $lte: 65}})
db.sales.find({ "customer.age": { $gte: 65}})

logical operator
1. and 
2. or


Lesson 1 - Inserting Documents
MongoDB Docs: insertOne()

MongoDB Docs: insertMany()

Lesson 2 - Finding Documents
MongoDB Docs: find()

MongoDB Docs: $in

Lesson 3 - Finding Documents Using Comparison Operators
MongoDB Docs: Comparison Operators
Lesson 4 - Querying on Array Elements
MongoDB Docs: $elemMatch

MongoDB Docs: Querying Arrays

Lesson 5 - Finding Documents Using Logical Operators
MongoDB Docs: Logical Operators






# deleting and modifying documentss
```
To replace documents in MongoDB, we use the replaceOne() method. The replaceOne() method takes the following parameters:

filter: A query that matches the document to replace.
replacement: The new document to replace the old one with.
options: An object that specifies options for the update.
In the previous video, we use the _id field to filter the document. In our replacement document, we provide the entire document that should be inserted in its place. Here's the example code from the video:

db.books.replaceOne(
  {
    _id: ObjectId("6282afeb441a74a98dbbec4e"),
  },
  {
    title: "Data Science Fundamentals for Python and MongoDB",
    isbn: "1484235967",
    publishedDate: new Date("2018-5-10"),
    thumbnailUrl:
      "https://m.media-amazon.com/images/I/71opmUBc2wL._AC_UY218_.jpg",
    authors: ["David Paper"],
    categories: ["Data Science"],
  }
)
```


in updateOne method of mongoDb the if there not matching recording the we insert a record and will created a new object_id

1. upsert
2. replace
3. update
4. push

```
The updateOne() method accepts a filter document, an update document, and an optional options object. MongoDB provides update operators and options to help you update documents. In this section, we'll cover three of them: $set, upsert, and $push.

$set
The $set operator replaces the value of a field with the specified value, as shown in the following code:

db.podcasts.updateOne(
  {
    _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8"),
  },

  {
    $set: {
      subscribers: 98562,
    },
  }
)
upsert
The upsert option creates a new document if no documents match the filtered criteria. Here's an example:

db.podcasts.updateOne(
  { title: "The Developer Hub" },
  { $set: { topics: ["databases", "MongoDB"] } },
  { upsert: true }
)
$push
The $push operator adds a new value to the hosts array field. Here's an example:

db.podcasts.updateOne(
  { _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8") },
  { $push: { hosts: "Nic Raboy" } }
)
```


>> Correct! The `updateOne()` method requires the use of an update operator to update a document, such as `$set`, `$push`, `$pop`, `$unset`, or `$inc`.


## findModify()
```
Updating MongoDB Documents by Using findAndModify()
The findAndModify() method is used to find and replace a single document in MongoDB. It accepts a filter document, a replacement document, and an optional options object. The following code shows an example:

db.podcasts.findAndModify({
  query: { _id: ObjectId("6261a92dfee1ff300dc80bf1") },
  update: { $inc: { subscribers: 1 } },
  new: true,
})
```

## updateMany()

```
Updating MongoDB Documents by Using updateMany()
To update multiple documents, use the updateMany() method. This method accepts a filter document, an update document, and an optional options object. The following code shows an example:

db.books.updateMany(
  { publishedDate: { $lt: new Date("2019-01-01") } },
  { $set: { status: "LEGACY" } }
)
```


there are two ways to delete the records in mongo
1. deleteOne 
2. deleteMany

```
Deleting Documents in MongoDB
To delete documents, use the deleteOne() or deleteMany() methods. Both methods accept a filter document and an options object.

Delete One Document
The following code shows an example of the deleteOne() method:

db.podcasts.deleteOne({ _id: Objectid("6282c9862acb966e76bbf20a") })
Delete Many Documents
The following code shows an example of the deleteMany() method:

db.podcasts.deleteMany({category: “crime”})
```


# MongoDB CRUD Operations: Replace and Delete Documents
In this unit, you learned how to modify query results with MongoDB. Specifically, you:

* Replaced a single document by using db.collection.replaceOne().
* Updated a field value by using the $set update operator in db.collection.updateOne().
* Added a value to an array by using the $push update operator in db.collection.updateOne().
* Added a new field value to a document by using the upsert option in db.collection.updateOne().
* Found and modified a document by using db.collection.findAndModify().
* Updated multiple documents by using db.collection.updateMany().
* Deleted a document by using db.collection.deleteOne().

# limiting and offset
```
Sorting and Limiting Query Results in MongoDB
Review the following code, which demonstrates how to sort and limit query results.

Sorting Results
Use cursor.sort() to return query results in a specified order. Within the parentheses of sort(), include an object that specifies the field(s) to sort by and the order of the sort. Use 1 for ascending order, and -1 for descending order.

Syntax:

db.collection.find(<query>).sort(<sort>)
Example:

// Return data on all music companies, sorted alphabetically from A to Z.
db.companies.find({ category_code: "music" }).sort({ name: 1 });
To ensure documents are returned in a consistent order, include a field that contains unique values in the sort. An easy way to do this is to include the _id field in the sort. Here's an example:

// Return data on all music companies, sorted alphabetically from A to Z. Ensure consistent sort order
db.companies.find({ category_code: "music" }).sort({ name: 1, _id: 1 });
Limiting Results
Use cursor.limit() to return query results in a specified order. Within the parentheses of limit(), specify the maximum number of documents to return.

Syntax:

db.companies.find(<query>).limit(<number>)
Example:

// Return the three music companies with the highest number of employees. Ensure consistent sort order.
db.companies
  .find({ category_code: "music" })
  .sort({ number_of_employees: -1, _id: 1 })
  .limit(3);
```

## select field returning and its called projections
```
Returning Specific Data from a Query in MongoDB
Review the following code, which demonstrates how to return selected fields from a query.

Add a Projection Document
To specify fields to include or exclude in the result set, add a projection document as the second parameter in the call to db.collection.find().

Syntax:

db.collection.find( <query>, <projection> )
Include a Field
To include a field, set its value to 1 in the projection document.

Syntax:

db.collection.find( <query>, { <field> : 1 })
Example:

// Return all restaurant inspections - business name, result, and _id fields only
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1 }
)
Exclude a Field
To exclude a field, set its value to 0 in the projection document.

Syntax:

db.collection.find(query, { <field> : 0, <field>: 0 })
Example:

// Return all inspections with result of "Pass" or "Warning" - exclude date and zip code
db.inspections.find(
  { result: { $in: ["Pass", "Warning"] } },
  { date: 0, "address.zip": 0 }
)
While the _id field is included by default, it can be suppressed by setting its value to 0 in any projection.

// Return all restaurant inspections - business name and result fields only
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1, _id: 0 }
)
```

## How to count the number of document in the list.
```
Counting Documents in a MongoDB Collection
Review the following code, which demonstrates how to count the number of documents that match a query.

Count Documents
Use db.collection.countDocuments() to count the number of documents that match a query. countDocuments() takes two parameters: a query document and an options document.

Syntax:

db.collection.countDocuments( <query>, <options> )
The query selects the documents to be counted.

Examples:

// Count number of docs in trip collection
db.trips.countDocuments({})
// Count number of trips over 120 minutes by subscribers
db.trips.countDocuments({ tripduration: { $gt: 120 }, usertype: "Subscriber" })
```


### MongoDB CRUD Operations: Modifying Query Results

In this unit, you learned how to modify query results with MongoDB. Specifically, you learned how to:

* Return query results in a specified order by using cursor.sort().

* Constrained the number of results returned by using cursor.limit().

* Specified fields to return by adding a projection document parameter in calls to db.collection.find().

* Counted the number of documents that match a query by using db.collection.countDocuments().




# aggregations
```
Using $match
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we used the $match and $group stages.

Use the $match operator to select documents that match the specified query condition(s) and pass the matching documents to the next stage. $match takes a document that specifies the query.

$match should be placed early in a pipeline to reduce the number of documents that will be processed later in the pipeline.

Here's an example of the $match stage:

# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

Using $group
Use the $group stage to separate documents into groups. The $group stage must have an _id field that specifies the group key. The group key is preceded by a $ and enclosed in quotation marks.

A $group stage can include additional field(s) that are computed by using accumulator operators, such as $avg.

Here's an example of the $group stage:

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

Aggregation Example That Uses $match and $group
The following is an example of an aggregation pipeline that uses $match and $group.

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()
```

Aggregation is a language for filtering, sorting, organizing and analyzing data,

Define aggregation and the components of an aggregation pipeline.
Build an aggregation pipeline that uses the $match and $group stages.
Build an aggregation pipeline that uses the $sort and $project stages.



```
Creating a Single Field Index
Review the code below, which demonstrates how to create a single field index in a collection.


Create a Single Field Index
Use createIndex() to create a new index in a collection. Within the parentheses of createIndex(), include an object that contains the field and sort order.

db.customers.createIndex({
  birthdate: 1
})

Create a Unique Single Field Index
Add {unique:true} as a second, optional, parameter in createIndex() to force uniqueness in the index field values. Once the unique index is created, any inserts or updates including duplicated values in the collection for the index field/s will fail.

db.customers.createIndex({
  email: 1
},
{
  unique:true
})
MongoDB only creates the unique index if there is no duplication in the field values for the index field/s.


View the Indexes used in a Collection
Use getIndexes() to see all the indexes created in a collection.

db.customers.getIndexes()

Check if an index is being used on a query
Use explain() in a collection when running a query to see the Execution plan. This plan provides the details of the execution stages (IXSCAN , COLLSCAN, FETCH, SORT, etc.).

The IXSCAN stage indicates the query is using an index and what index is being selected.
The COLLSCAN stage indicates a collection scan is perform, not using any indexes.
The FETCH stage indicates documents are being read from the collection.
The SORT stage indicates documents are being sorted in memory.
db.customers.explain().find({
  birthdate: {
    $gt:ISODate("1995-08-01")
    }
  })
db.customers.explain().find({
  birthdate: {
    $gt:ISODate("1995-08-01")
    }
  }).sort({
    email:1
    })

```


# Multikey indexing in MongoDB:

* Any index where one of the indexed fields contains an array.
* The array can hold nested objects or other field types
* In a compound index only one field can be an array per index.

# Compound indexex
* Index on multiple fields 
* can be a multikey index if it includes an array fields 
* maximum of one array field per index.
* Support queries that match on the prefix of the index fields
```
Working with Compound Indexes
Review the code below, which demonstrates how to create a compound index in a collection.


Create a Compound Index
Use createIndex() to create a new index in a collection. Within the parentheses of createIndex(), include an object that contains two or more fields and their sort order.

db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})

Order of Fields in a Compound Index
The order of the fields matters when creating the index and the sort order. It is recommended to list the fields in the following order: Equality, Sort, and Range.

Equality: field/s that matches on a single field value in a query
Sort: field/s that orders the results by in a query
Range: field/s that the query filter in a range of valid values
The following query includes an equality match on the active field, a sort on birthday (descending) and name (ascending), and a range query on birthday too.

db.customers.find({
  birthdate: {
    $gte:ISODate("1977-01-01")
    },
    active:true
    }).sort({
      birthdate:-1, 
      name:1
      })
Here's an example of an efficient index for this query:

db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})

View the Indexes used in a Collection
Use getIndexes() to see all the indexes created in a collection.

db.customers.getIndexes()

Check if an index is being used on a query
Use explain() in a collection when running a query to see the Execution plan. This plan provides the details of the execution stages (IXSCAN , COLLSCAN, FETCH, SORT, etc.). Some of these are:

The IXSCAN stage indicates the query is using an index and what index is being selected.
The COLLSCAN stage indicates a collection scan is perform, not using any indexes.
The FETCH stage indicates documents are being read from the collection.
The SORT stage indicates documents are being sorted in memory.
db.customers.explain().find({
  birthdate: {
    $gte:ISODate("1977-01-01")
    },
  active:true
  }).sort({
    birthdate:-1,
    name:1
    })

Cover a query by the Index
An Index covers a query when MongoDB does not need to fetch the data from memory since all the required data is already returned by the index.

In most cases, we can use projections to return only the required fields and cover the query. Make sure those fields in the projection are in the index.

By adding the projection {name:1,birthdate:1,_id:0} in the previous query, we can limit the returned fields to only name and birthdate. These fields are part of the index and when we run the explain() command, the execution plan shows only two stages:

IXSCAN - Index scan using the compound index
PROJECTION_COVERED - All the information needed is returned by the index, no need to fetch from memory
db.customers.explain().find({
  birthdate: {
    $gte:ISODate("1977-01-01")
    },
  active:true
  },
  {name:1,
    birthdate:1, 
    _id:0
  }).sort({
    birthdate:-1,
    name:1
    })
```

# How to delete index in the 
```
Deleting an Index
Review the code below, which demonstrates how to delete indexes in a collection.


View the Indexes used in a Collection
Use getIndexes() to see all the indexes created in a collection. There is always a default index in every collection on _id field. This index is used by MongoDB internally and cannot be deleted.

db.customers.getIndexes()

Delete an Index
Use dropIndex() to delete an existing index from a collection. Within the parentheses of dropIndex(), include an object representing the index key or provide the index name as a string.

Delete index by name:

db.customers.dropIndex(
  'active_1_birthdate_-1_name_1'
)
Delete index by key:

db.customers.dropIndex({
  active:1,
  birthdate:-1, 
  name:1
})

Delete Indexes
Use dropIndexes() to delete all the indexes from a collection, with the exception of the default index on _id.

db.customers.dropIndexes()
The dropIndexes() command also can accept an array of index names as a parameter to delete a specific list of indexes.

db.collection.dropIndexes([
  'index1name', 'index2name', 'index3name'
  ])
```