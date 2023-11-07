"""1. Calcule el promedio, el menor valor y el mayor valor de los pesos de N paquetes en una bodega"""

# Variables de entrada.
# - cantidad de paquetes.

# Variables de salida.
# - promedio de los pesos.
# - peso mayor.
# - peso menor.

from ValidacionDeDatos import *

numeroPaquetes = ValidarEntero("Ingrese el número de paquetes: ")

pesoMayor = 0
pesoMenor = 10000
promedioPesos = 0                   # variables para almacenar las salidas.

sumaPesos = 0                       # acumular la suma de los pesos de los paquetes.

for i in range (0, numeroPaquetes):
    pesoPaquetes = ValidarReal("\nIngrese el peso del paquete (en Kgs): ")

    sumaPesos += pesoPaquetes

    if pesoPaquetes > pesoMayor:
        pesoMayor = pesoPaquetes

    if pesoPaquetes < pesoMenor:
        pesoMenor = pesoPaquetes

promedioPesos = sumaPesos / numeroPaquetes
print("\nEl peso promedio de los paquetes es: ",format(promedioPesos, ".3f"), " Kgs.")

print("El peso mayor es: ", pesoMayor, " Kgs.")
print("El peso menor es: ", pesoMenor, " Kgs.")
