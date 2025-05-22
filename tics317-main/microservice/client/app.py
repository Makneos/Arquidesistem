import requests

BASE_TASK_URL = "http://localhost:5001"
BASE_LOG_URL = "http://localhost:5003"

def menu():
    print("\n=== Gestor de Tareas ===")
    print("1. Listar tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Ver logs")
    print("0. Salir")

def list_tasks():
    response = requests.get(f"{BASE_TASK_URL}/tasks")
    tasks = response.json()
    for t in tasks:
        estado = "✅" if t['completed'] else "❌"
        print(f"{t['id']}. {t['title']} - {estado}")

def add_task():
    title = input("Título de la tarea: ")
    data = {"title": title}
    requests.post(f"{BASE_TASK_URL}/tasks", json=data)

def complete_task():
    task_id = input("ID de la tarea a completar: ")
    requests.put(f"{BASE_TASK_URL}/tasks/{task_id}/complete")

def delete_task():
    task_id = input("ID de la tarea a eliminar: ")
    requests.delete(f"{BASE_TASK_URL}/tasks/{task_id}")

def view_logs():
    response = requests.get(f"{BASE_LOG_URL}/logs")
    print("\n=== LOGS ===")
    print(response.text)

if __name__ == "__main__":
    while True:
        menu()
        option = input("Selecciona una opción: ")
        if option == "1":
            list_tasks()
        elif option == "2":
            add_task()
        elif option == "3":
            complete_task()
        elif option == "4":
            delete_task()
        elif option == "5":
            view_logs()
        elif option == "0":
            break
        else:
            print("Opción no válida.")
