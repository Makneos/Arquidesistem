from models.task import Task
from storage.task_repo import TaskRepository
from views.task_view import TaskView

class TaskController:
    def __init__(self):
        self.repo = TaskRepository()
        self.view = TaskView()

    def run(self):
        while True:
            self.view.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                titulo, descripcion = self.view.pedir_datos_tarea()
                tarea = Task(titulo, descripcion)
                self.repo.agregar_tarea(tarea)
                self.view.mostrar_mensaje("Tarea agregada.")
            elif opcion == "2":
                tareas = self.repo.obtener_tareas()
                self.view.mostrar_tareas(tareas)
            elif opcion == "3":
                tareas = self.repo.obtener_tareas()
                self.view.mostrar_tareas(tareas)
                indice = self.view.pedir_indice()
                if 0 <= indice < len(tareas):
                    tareas[indice].completada = True
                    self.repo.guardar_tareas(tareas)
                    self.view.mostrar_mensaje("Tarea marcada como completada.")
                else:
                    self.view.mostrar_mensaje("Índice inválido.")
            elif opcion == "4":
                tareas = self.repo.obtener_tareas()
                self.view.mostrar_tareas(tareas)
                indice = self.view.pedir_indice()
                if 0 <= indice < len(tareas):
                    self.repo.eliminar_tarea(indice)
                    self.view.mostrar_mensaje("Tarea eliminada.")
                else:
                    self.view.mostrar_mensaje("Índice inválido.")
            elif opcion == "5":
                self.view.mostrar_mensaje("Hasta luego.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")
