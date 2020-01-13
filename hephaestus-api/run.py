from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Seems fine"


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False,
            passthrough_errors=True)
