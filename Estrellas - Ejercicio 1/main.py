from vector3d import Vector3D
from sol import Sol
from proxima_centauri import ProximaCentauri
from alpha_centauri import AlphaCentauri
from capella import Capella
from galaxia import Galaxia

# Creación de estrellas
estrellas = [
    Sol(),
    ProximaCentauri(),
    AlphaCentauri(),
    Capella(),
]

# Creación de galaxias y asignación de estrellas
galaxias = {}
for estrella in estrellas:
    if estrella.galaxia not in galaxias:
        galaxias[estrella.galaxia] = Galaxia(estrella.galaxia)
    galaxias[estrella.galaxia].agregar_estrella(estrella)

# Mostrar información de estrellas y galaxias
for estrella in estrellas:
    print(f"Estrella {estrella.nombre} en {estrella.posicion}, Galaxia {estrella.galaxia}")

for nombre, galaxia in galaxias.items():
    print(galaxia)

print(f"Universo con {len(galaxias)} galaxias: {', '.join(galaxias.keys())}")
