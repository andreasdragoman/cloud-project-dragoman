import database as db
import face_service as fs

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    results = db.getInventory()
    return str(results[0])
