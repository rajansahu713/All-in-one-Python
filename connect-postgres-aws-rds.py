import psycopg2
connection = psycopg2.connect(
    host = 'endpoint',
    port = "port number",
    user = 'username',
    password = 'password',
    database='database name'
    )
cursor=connection.cursor()
cursor.execute("""CREATE TABLE rand1(
id SERIAL PRIMARY KEY,
name text)""")

connection.commit()