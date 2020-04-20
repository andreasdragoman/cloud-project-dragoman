import mysql.connector
from mysql.connector import errorcode

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
