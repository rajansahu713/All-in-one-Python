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
cursor.execute("select * from student")

students = cursor.fetchall()

for student in students:
    print(student)

print("Fetching alll the record");
  
# Closing the connection
conn.close()