import database as db
import faceservice as fs

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    results = db.getInventory()
    return str(results[0])
