import os
from intro_to_flask import app

port = int(os.environ.get("PORT", 5000))

from flask import Flask,render_template,request,redirect,url_for,jsonify,make_response,flash
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb+srv://badnagar123:badnagar123@covid-help-badnagar.w92qq.mongodb.net/Covid_Data?retryWrites=true&w=majority"
#app.secret_key='dont tell anyone'
#app.config["MONGO_URI"] = "mongodb+srv://apecskaam:apecs123@apecs.gucd9.mongodb.net/APECS_User_Data?retryWrites=true&w=majority"


@app.route('/',methods=['POST','GET'])
def base():
    return render_template("<h1>This is done</h1>")
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=port) 
