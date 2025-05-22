from flask import Flask, request
import datetime

app = Flask(__name__)
LOG_FILE = "log.txt"

@app.route("/")
def home():
    return "Logging Service Activo"

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {data.get('message')}\n")
    return {"status": "logged"}, 201

@app.route("/logs")
def get_logs():
    with open(LOG_FILE, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(port=5003)
