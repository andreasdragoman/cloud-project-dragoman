import database as db
import faceservice as fs

from flask import Flask, render_template, request, Response
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
  if request.method == 'GET':
    return render_template("home.html")
  if request.method == 'POST':
    data = request.form
    results = db.getInventory()
    #return str(results[0])
    results = fs.getFaceInfoFromURL()
    # if results is not None:
    #   return str(results)
    return render_template("home.html", imageFaceInfoResult=results)
