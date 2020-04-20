import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'cloud-project-serverdb.mysql.database.azure.com',
  'user':'DragomanDbUser@cloud-project-serverdb',
  'password':'Portocale1',
  'database':'cloudcomputing'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  
def getTestRecords():
  # Read data
  cursor.execute("SELECT * FROM test;")
  rows = cursor.fetchall()
  return rows
  
