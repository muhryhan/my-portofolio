from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def porto():
    return render_template('index.html')

@app.route("/contme", methods=["POST"])
def contme_post():
    name_receive = request.form['name_give']
    mail_receive = request.form['mail_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name' : name_receive,
        'mail' : mail_receive,
        'messages' : comment_receive
    }
    db.messages.insert_one(doc)

    return jsonify({'msg':'POST request!'})

# running program
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)