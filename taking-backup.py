import subprocess

# Set the name of the database to be backed up
database_name = 'mydatabase'

# Set the username and password for the MySQL server
username = 'root'
password = 'password'

# Set the file path for the backup file
file_path = 'mydatabase_backup.sql'

# Run the mysqldump command to take the backup
subprocess.run(['mysqldump', '-u' + username, '-p' + password, database_name], stdout=open(file_path, 'w'))

print("Backup created successfully at", file_path)
