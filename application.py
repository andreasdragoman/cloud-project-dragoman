import database as db
import faceservice as fs

from flask import Flask, render_template, request, Response
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
  results = db.getInventory()
  #return str(results[0])
  results = fs.getFaceInfoFromURL()
  # if results is not None:
  #   return str(results)
  return render_template("home.html")


@app.route("/", methods=["POST"])
def hello():
  results = db.getInventory()
  #return str(results[0])
  results = fs.getFaceInfoFromURL()
  # if results is not None:
  #   return str(results)
  return render_template("home.html")
