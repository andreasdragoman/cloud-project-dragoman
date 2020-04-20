import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'cloud-project-serverdb.mysql.database.azure.com',
  'user':'DragomanDbUser@cloud-project-serverdb',
  'password':'Portocale1',
  'database':'cloudcomputing'
}

is_connected = False

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
  is_connected = True
  cursor = conn.cursor()


def createTables():
  if is_connected == True:
    cursor.execute("DROP TABLE IF EXISTS inventory;")
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    conn.commit()
    return True
  else:
    return False
  

def insertItemInInventory(item_name, item_quantity):
  if is_connected == True:
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", (item_name, item_quantity))
    conn.commit()
    return True
  else:
    return False
  
  
def getInventory():
  if is_connected == True:
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()
    return rows
  else:
    return null
  

def updateInventoryItem(item_id, item_name, item_quantity):
  if is_connected == True:
    cursor.execute("UPDATE inventory SET name = %s, quantity = %s WHERE id = %d;", (item_name, item_quantity, item_id))
    conn.commit()
    return True
  else:
    return False
  
  
def deleteInventoryItem(item_id):
  if is_connected == True:
    cursor.execute("DELETE FROM inventory WHERE id=%(param1)d;", {'param1':item_id})
    conn.commit()
    return True
  else:
    return False
    
   
def cleanUpConnection():
  conn.commit()
  cursor.close()
  conn.close()
  
  
