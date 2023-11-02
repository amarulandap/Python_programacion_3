import math
import random
from math import *
import ValidacionDeDatos

"""1. Simular el lamzamiento de un dado"""

# Crear una variable donde almacenar el resultado del lanzamiento.
valorDado = 0
numeroIntentos = 0

while valorDado != 3:
    valorDado = random.randint(1, 6)
    numeroIntentos += 1

print(valorDado, "Número de intentos:", numeroIntentos)


"""2. Suma de los cuadrados de los n números naturales"""

# Solicitar el número de naturales a sumar.
while True:
    cantidadNumeros = ValidacionDeDatos.ValidarEntero("¿Cúantos números naturales desea sumar? ")
    if cantidadNumeros > 0:
        break;

# Crear la variable contadora.
contador1 = 0

# Crear las variables para almacenar cada uno de los números enteros y la suma de sus cuadrados.
numeroEntero = 1
sumaNumerosEnteros = 0

while contador1 < cantidadNumeros:
    cuadrado = math.pow(numeroEntero, 2)
    sumaNumerosEnteros += cuadrado

    numeroEntero += 1
    contador1 += 1

print("Suma = ", sumaNumerosEnteros)


"""3. Conteo de bacterias."""

# Cantidad inicial de bacterias.
cantidadInicial = ValidacionDeDatos.ValidarEntero("Cantidad inicial de bacterias: ")
cantidadMaxima = ValidacionDeDatos.ValidarEntero("Cantidad máxima de bacterias: ")

# Contador de días
dia = 0

cantidadBacterias = cantidadInicial
while cantidadBacterias <= cantidadMaxima:
    dia += 1
    cantidadBacterias *= 2

print("la cantidad excedió el máximo en el día: ", dia)

# En Python, no existe la estructura Do - while, pero se puede implementar a través de un while True en combinación
# con una instrucción break.

