from vector3d import Vector3D

class Planeta:
    def __init__(self, nombre, posicion, tiene_vida=False):
        self.nombre = nombre
        self.posicion = posicion
        self.tiene_vida = tiene_vida
