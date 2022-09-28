from flask import (
    Flask,
    jsonify,


)

app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route("/")
def home():
    return jsonify(
        mesage="Your first endpoint is working")
