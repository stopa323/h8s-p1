from flask import Flask, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/hephaestus_db"
mongo = PyMongo(app)


@app.route("/")
def index():
    a = mongo.db.blueprints.find()
    res = []
    for x in a:
        res.append(x['key'])

    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False,
            passthrough_errors=True)
