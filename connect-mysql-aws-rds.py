import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='endpoint',
                             user='username',
                             password='password',
                             database='database name',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        for i in range(1, 1000):
            sql = f"INSERT INTO Persons VALUES ({i},'raj{i}') "
            cursor.execute(sql)
    connection.commit()