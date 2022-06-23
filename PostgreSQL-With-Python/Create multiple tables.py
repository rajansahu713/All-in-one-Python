import psycopg2
  
conn = psycopg2.connect(
   database="demo",
    user='postgres',
    password='*********',
    host='localhost',
    port= '5432'
)
  
conn.autocommit = True
  
# Creating a cursor object
cursor = conn.cursor()
  
# query to create a database 
sql = (
    '''
        CREATE TABLE Items (
            item_id SERIAL PRIMARY KEY,
            item_name VARCHAR(255) NOT NULL
        )''',
    '''
        CREATE TABLE Cricketers (
           first_Name VARCHAR(255),
           last_Name VARCHAR(255),
           age INT,
           place_Of_Birth VARCHAR(255),
           country VARCHAR(255)
    )'''
      )

# executing above query
for table in sql:
    cursor.execute(table)
print("Tables has been created successfully !!");
  
# Closing the connection
conn.close()