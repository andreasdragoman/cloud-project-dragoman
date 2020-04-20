import database as db

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    records = db.getTestRecords();
    return str(records[0])

