"""Conociendo las coordenadas de la fábrica, y los sitios de distribución, encontrar el mas alejado"""

# Variables de entrada:
# Coordenadas de la fabrica
# Número de puntos de distribución.
# Coordenadas del punto.

# Variables de salida:
# Distancia mayor.

# Procesos.
# Solicitar las coordenadas de la fabrica y almacenarlas en una lista.
# Solicitar el número de puntos de distribución.
# Solicitar las coordenadas de cada punto.
# Calcular la distancia a la fabrica de cada punto.
# Alamcenar cada distancia en una lista.
# Hallar el mayor valor en la lista de distancias.

from ValidacionDeDatos import *
from math import *

coordenadasFabrica = [ ]
coordenadaXFabrica = ValidarReal("Primera coordenada de la fabrica: ")          # Coordenada X de la fabrica.
coordenadasFabrica.append(coordenadaXFabrica)
coordenadaYFabrica = ValidarReal("Segunda coordenada de la fabrica: ")          # Coordenada Y de la fabrica,
coordenadasFabrica.append(coordenadaYFabrica)

puntosDistribucion = ValidarEntero("Número de puntos de distribución: ")        # Total puntos de distribución.

contadorPuntos = 0
coordenadasPunto = [ ]                             # Lista que almacena cada corrdenada de los puntos.
distanciaPuntos = [ ]                              # Lista que almacena las distancias.

while contadorPuntos < puntosDistribucion:

    coordenadaXPunto = ValidarReal("Primera coordenada del punto: ")            # Coordenada X del punto.
    coordenadasPunto.append(coordenadaXPunto)
    coordenadaYPunto = ValidarReal("Segunda coordenada del punto: ")            # Coordenada Y del punto.
    coordenadasPunto.append(coordenadaYPunto)

    distanciaFabrica = sqrt(pow(coordenadaXFabrica - coordenadaXPunto, 2) + pow(coordenadaYFabrica - coordenadaYPunto, 2))
    distanciaPuntos.append(distanciaFabrica)

    del coordenadasPunto[:2]                       # Borrar las coordenadas del punto para ingresar unas nuevas.

    contadorPuntos += 1

distanciaMayor = 0                                 # Almacenar la distancia que deseamos encontrar.
contadorDistancias = 0
while contadorDistancias < len(distanciaPuntos):
    if distanciaPuntos[contadorDistancias] > distanciaMayor:
        distanciaMayor = distanciaPuntos[contadorDistancias]

    contadorDistancias += 1

print("La mayor distancia es: ",format(distanciaMayor, ".3f"), " punto número: ", distanciaPuntos.index(distanciaMayor))




