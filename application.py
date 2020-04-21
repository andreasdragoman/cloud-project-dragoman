from flask import Flask, render_template, request, Response, jsonify
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template("home.html")
  
  
@app.route('/getImageInfoFromURL', methods=['POST'])
def getImageInfoFromURL():
  return "ok"
