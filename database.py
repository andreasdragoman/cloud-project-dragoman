import mysql.connector
from mysql.connector import errorcode


config = {
  'host':'cloud-project-serverdb.mysql.database.azure.com',
  'user':'DragomanDbUser@cloud-project-serverdb',
  'password':'Portocale1',
  'database':'cloudcomputing'
}


def createTables():
  global config
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return False
  else:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    cursor.execute("CREATE TABLE FacesDetectedInfo (id serial PRIMARY KEY, url VARCHAR(50), response VARCHAR(50));")
    conn.commit()
    cursor.close()
    conn.close()
    return True
  

def insertItemInInventory(item_name, item_quantity):
  global config
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return False
  else:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", (item_name, item_quantity))
    conn.commit()
    cursor.close()
    conn.close()
    return True
  
  
def getInventory():
  global config 
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return None
  else:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows
  
  
def updateInventoryItem(item_id, item_name, item_quantity):
  global config
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return False
  else:
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET name = %s, quantity = %s WHERE id = %d;", (item_name, item_quantity, item_id))
    conn.commit()
    cursor.close()
    conn.close()
    return True
  
  
def deleteInventoryItem(item_id):
  global config
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return False
  else:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id=%d;", (item_id))
    conn.commit()
    cursor.close()
    conn.close()
    return True
  
  
def insertInFacesDetectedInfo(item_url, item_result):
  global config
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return False
  else:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FacesDetectedInfo (url, result) VALUES (%s, %s);", (item_url, item_result))
    conn.commit()
    cursor.close()
    conn.close()
    return True
  
  
def getFacesDetectedInfo():
  global config 
  try:
    conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    return None
  else:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FacesDetectedInfo;")
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows
