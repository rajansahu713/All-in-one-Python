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
cursor.execute("Update student set student_name = %s where student_id = %s", ("Munmi",1))

print("Records has been updated successfully !!");
  
# Closing the connection
conn.close()