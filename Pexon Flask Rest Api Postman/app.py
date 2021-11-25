from flask import Flask, Blueprint, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run()