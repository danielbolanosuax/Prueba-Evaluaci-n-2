class Galaxia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sistemas = []

    def agregar_sistema(self, sistema):
        self.sistemas.append(sistema)

    def info(self):
        return f"Galaxia {self.nombre} con {len(self.sistemas)} sistemas solares."
