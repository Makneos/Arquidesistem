import json
import os
from models.task import Task

DATA_FILE = os.path.join(os.path.dirname(__file__), "task.json")

class TaskRepository:
    def obtener_tareas(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as archivo:
            data = json.load(archivo)
            return [Task.from_dict(d) for d in data]

    def guardar_tareas(self, tareas):
        with open(DATA_FILE, "w") as archivo:
            json.dump([t.to_dict() for t in tareas], archivo, indent=4)

    def agregar_tarea(self, tarea):
        tareas = self.obtener_tareas()
        tareas.append(tarea)
        self.guardar_tareas(tareas)

    def eliminar_tarea(self, indice):
        tareas = self.obtener_tareas()
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            self.guardar_tareas(tareas)
