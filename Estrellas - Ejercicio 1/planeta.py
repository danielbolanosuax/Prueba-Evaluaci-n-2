class Planeta:
    def __init__(self, nombre, tiene_vida=False):
        self.nombre = nombre
        self.tiene_vida = tiene_vida

    def info(self):
        estado_vida = "con vida" if self.tiene_vida else "sin vida"
        return f"{self.nombre}, un planeta {estado_vida}."
