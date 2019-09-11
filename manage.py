from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the home Page </h1>"


@app.route("/about")
def about():
    return jsonify({
        "age": 45,
        "Sex": "Male"
    })


if __name__ == "__main__":
    app.run(debug=True)
