from flask import Flask
app = Flask(__name__)

conn = mysql.connector.connect(user='DragomanDbUser@cloud-project-serverdb',
                                   password='Portocale1',
                                   database='cloudcomputing',
                                   host='cloud-project-serverdb.mysql.database.azure.com',
                                   ssl_ca='/var/www/html/BaltimoreCyberTrustRoot.crt.pem')
except mysql.connector.Error as err:
    print(err)

@app.route("/")
def hello():
    return "Hello World!"
