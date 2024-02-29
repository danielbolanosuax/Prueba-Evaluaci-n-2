from proxima_centauri import ProximaCentauri
from alpha_centauri import AlphaCentauri
from capella import Capella
from sol import Sol
from planeta import Planeta
from sistema_solar import SistemaSolar
from galaxia import Galaxia

# Crear estrellas específicas
proxima_centauri = ProximaCentauri()
alpha_centauri = AlphaCentauri()
capella = Capella()
sol = Sol()

# Crear planetas
tierra = Planeta("Tierra", tiene_vida=True)
marte = Planeta("Marte", tiene_vida=False)

# Crear sistema solar y agregar estrellas y planetas
sistema_solar = SistemaSolar("Sistema Solar")
sistema_solar.agregar_cuerpo(sol)
sistema_solar.agregar_cuerpo(tierra)
sistema_solar.agregar_cuerpo(marte)

# Crear galaxia y agregar sistemas solares
via_lactea = Galaxia("Vía Láctea")
via_lactea.agregar_sistema(sistema_solar)

# Imprimir información de la galaxia, sistemas solares, estrellas y planetas
print(via_lactea.info())
for sistema in via_lactea.sistemas:
    print(sistema.info())
    for cuerpo in sistema.cuerpos:
        print(cuerpo.info())

# Opcionalmente, agregar más sistemas solares o cuerpos celestes y repetir el proceso de impresión
