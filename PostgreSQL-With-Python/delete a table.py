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
  

# executing above query
cursor.execute("DROP table student")

print("Table has been deleted")
  
# Closing the connection
conn.close()