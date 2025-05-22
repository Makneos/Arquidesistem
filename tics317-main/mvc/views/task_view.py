class TaskView:
    def mostrar_menu(self):
        print("\n==== TODO APP ====")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

    def pedir_datos_tarea(self):
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        return titulo, descripcion

    def mostrar_tareas(self, tareas):
        if not tareas:
            print("No hay tareas.")
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i + 1}. {tarea.titulo} - {tarea.descripcion} [{estado}]")

    def pedir_indice(self):
        try:
            return int(input("Número de tarea: ")) - 1
        except ValueError:
            return -1

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
