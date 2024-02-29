from vector3d import Vector3D
import math

def calcular_distancia_entre_cuerpos(cuerpo1, cuerpo2):
    diferencia = cuerpo1.posicion - cuerpo2.posicion
    return math.sqrt(diferencia.x ** 2 + diferencia.y ** 2 + diferencia.z ** 2)

def es_habitable(planeta):
    # Esta es una simplificación; los criterios reales son más complejos
    return planeta.tiene_vida
