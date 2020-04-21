import database as db
import faceservice as fs
import translateservice as ts

from flask import Flask, render_template, request, Response, jsonify
app = Flask(__name__)


@app.before_first_request
def create_tables():
    db.createTables()


@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template("home.html")
  
  
@app.route('/getImageInfoFromURL', methods=['POST'])
def getImageInfoFromURL():
  data = request.form
  results = fs.getFaceInfoFromURL(data['imgUrl'])
  resultTranslated = ts.getTranslatedText(results, data['targetLanguage'])
  db.insertInFacesDetectedInfo(data['imgUrl'], results, resultTranslated)
  return results
