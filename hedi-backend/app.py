import os

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import DecisionTree


@app.route("/")
def hello_world():
    return "Hello from HeDi!"


@app.route("/result/", methods=['POST'])
@cross_origin()
def result():
    payload = request.get_json()
    return jsonify(payload)


@app.route("/add-tree/", methods=['POST'])
def add_tree():
    payload = dict(request.get_json())
    decision_tree = DecisionTree(payload)
    db.session.add(decision_tree)
    db.session.commit()
    return "SAVED"


@app.route("/get-trees/", methods=['GET'])
def get_trees():
    decision_trees = DecisionTree.query.all()
    return jsonify([t.serialize() for t in decision_trees])


if __name__ == "__main__":
    app.run()
