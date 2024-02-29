class SistemaSolar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuerpos_celestes = []

    def agregar_cuerpo(self, cuerpo):
        self.cuerpos_celestes.append(cuerpo)
