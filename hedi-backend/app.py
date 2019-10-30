from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from HeDi!"


@app.route("/result/", methods=['POST'])
def result():
    payload = request.get_json()
    return jsonify(payload)


if __name__ == "__main__":
    app.run()
