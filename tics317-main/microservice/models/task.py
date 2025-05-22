class Task:
    def __init__(self, titulo, descripcion, completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["titulo"],
            data["descripcion"],
            data["completada"]
        )
