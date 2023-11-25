

import cx_Oracle
try:
    with cx_Oracle.connect(
            user="username", # Username
            password="password", # Password
            dsn="dsn", # End point
            encoding="encoding") as connection:
    # show the version of the Oracle Database
        print(connection.version)
        cursor = connection.cursor()
        cursor.execute("""create table employee(
            name varchar2(30), salary number(10, 2))""")   
        connection.commit()
except cx_Oracle.Error as error:
    print(f"Error {error}")




