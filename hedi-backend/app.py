import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from helper import DiagnosisRequest
from decision_tree import DecisionTreeClassifier
from models import DecisionTree


@app.route("/")
def hello_world():
    return "Hello from HeDi!"


@app.route("/result/", methods=['POST'])
def result():
    payload = request.get_json()
    diagnosis_data = DiagnosisRequest(payload)
    x_test = diagnosis_data.to_np_array()

    tree_model = DecisionTree.query.order_by(DecisionTree.id.desc()).first()
    decision_tree = tree_model.tree
    tree_classifier = DecisionTreeClassifier(initial_tree=decision_tree)

    prediction = tree_classifier.predict(x_test)
    response = {'result': prediction.tolist()[0]}
    return jsonify(response)


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
