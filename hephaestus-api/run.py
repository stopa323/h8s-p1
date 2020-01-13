import configparser
from flask import Flask, jsonify
from flask_pymongo import PyMongo

conf = configparser.ConfigParser()
conf.read("../etc/hephaestus.ini")

app = Flask(__name__)
app.config["MONGO_URI"] = conf.get("db", "connection")
mongo = PyMongo(app)


@app.route("/")
def index():
    a = mongo.db.blueprints.find()
    res = []
    for x in a:
        res.append(x['key'])

    return jsonify(res)


if __name__ == "__main__":
    debug = conf.get("DEFAULT", "debug")
    port = conf.get("DEFAULT", "bind_port")

    app.run(debug=debug, use_debugger=False, use_reloader=False,
            passthrough_errors=True, port=port)
