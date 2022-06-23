import psycopg2
  
conn = psycopg2.connect(
   database="postgres",
    user='postgres',
    password='*********',
    host='localhost',
    port= '5432'
)
  
conn.autocommit = True
  
# Creating a cursor object
cursor = conn.cursor()
  
# query to create a database 
sql = ''' DROP database demo ''';
  
# executing above query
cursor.execute(sql)
print("Database has been successfully delete !!");
  
# Closing the connection
conn.close()