from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

STORAGE_URL = "http://localhost:5002/storage/tasks"
LOGGING_URL = "http://localhost:5003/log"

@app.route("/")
def home():
    return "Task Service Activo"

def load_tasks():
    res = requests.get(STORAGE_URL)
    return res.json()

def save_tasks(tasks):
    requests.post(STORAGE_URL, json=tasks)

def log_event(msg):
    requests.post(LOGGING_URL, json={"message": msg})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get("title"),
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    log_event(f"Tarea creada: {new_task['title']}")
    return new_task, 201

@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            log_event(f"Tarea completada: {task['title']}")
            break
    save_tasks(tasks)
    return {"status": "completed"}

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    task_title = ""
    new_tasks = []
    for task in tasks:
        if task["id"] == task_id:
            task_title = task["title"]
        else:
            new_tasks.append(task)
    save_tasks(new_tasks)
    log_event(f"Tarea eliminada: {task_title}")
    return {"status": "deleted"}

if __name__ == "__main__":
    app.run(port=5001)
