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
sql = '''
        CREATE TABLE student (
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR(255) NOT NULL,
            student_address VARCHAR(255) NOT NULL
        ) ''';
  
# executing above query
cursor.execute(sql)
print("Table has been created successfully !!");
  
# Closing the connection
conn.close()