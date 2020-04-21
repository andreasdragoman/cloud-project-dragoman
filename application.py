import database as db
import faceservice as fs

from flask import Flask, render_template, request, Response, jsonify
app = Flask(__name__)


@app.before_first_request
def create_initial_tables():
    db.create_tables()


@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template("home.html")
  
  
@app.route('/getImageInfoFromURL', methods=['POST'])
def getImageInfoFromURL():
  data = request.form
  results = fs.getFaceInfoFromURL(data['imgUrl'])
  return results
