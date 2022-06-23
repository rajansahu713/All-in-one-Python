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
data = ('Rahul','Mumbai')

# executing above query
cursor.execute("INSERT into student(student_name, student_address) VALUES (%s, %s)", data)

print("Records has been inserted successfully !!");
  
# Closing the connection
conn.close()