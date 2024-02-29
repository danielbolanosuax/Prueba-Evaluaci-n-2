class SistemaSolar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuerpos = []

    def agregar_cuerpo(self, cuerpo):
        self.cuerpos.append(cuerpo)

    def info(self):
        return f"Sistema Solar {self.nombre} con {len(self.cuerpos)} cuerpos celestes."
