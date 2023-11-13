"""Mostrar dos números aleatorios cuya suma es un número primo"""

# Numero1, numero2
# Mensaje mostrando los dos números.

# generar los dos números de manera aleatoria.
# Sumarlos.
# Crear una lista para almacenar los divisores de la suma.
# Validar si la suma es un número primo.
# Mostrar en pantalla la pareja de números.

from random import *
from ValidacionDeDatos import *

numero1 = randint(1, 100)
numero2 = randint(1, 100)

sumaNumeros = 0
sumaNumeros = numero1 + numero2

listaDivisores = [ ]
for i in range(1, sumaNumeros + 1):

    if sumaNumeros % i == 0:
        listaDivisores.append(i)

if len(listaDivisores) > 2:
    print("Los números : ",numero1," y ",numero2, " no son números primos.")
else:
    print("Los números : ", numero1, " y ", numero2, " son números primos.")


"""Simulación del juego de las 3 ranas."""

# rana1, rana2, rana3
# 1 : Salta y queda en el mismo lugar.
# 2 : Salta 0.5 metros hacia adelante.
# 3 : Salta 1 metro hacia adelante.
# 4 : Salta 0.5 metros hacia atras.

# saltoRana1, saltoRana2, saltoRana3
# largoPista
# avanceRana1, avanceRana2, avanceRana3

# Ubicar las ranas en el principio de la pista.
# Generar el salto de la rana1


rana1 = 0               # Almacenar los avances de cada rana.
rana2 = 0
rana3 = 0

saltoRana1 = 0.0        # Almacenar el resultado de cada turno.
saltoRana2 = 0.0
saltoRana3 = 0.0

largoPista = ValidarReal("\nIngrese el largo de la pista: ")

while rana1 < largoPista and rana2 < largoPista and rana3 < largoPista:

    saltoRana1 = randint(1, 4)
    if saltoRana1 == 1:
        rana1 += 0
    elif saltoRana1 == 2:
        rana1 += 0.5
    elif saltoRana1 == 3:
        rana1 += 1
    elif saltoRana1 == 4:
        rana1 -= 0.5

    saltoRana2 = randint(1, 4)
    if saltoRana2 == 1:
        rana2 += 0
    elif saltoRana2 == 2:
        rana2 += 0.5
    elif saltoRana2 == 3:
        rana2 += 1
    elif saltoRana2 == 4:
        rana2 -= 0.5

    saltoRana3 = randint(1, 4)
    if saltoRana3 == 1:
        rana3 += 0
    elif saltoRana3 == 2:
        rana3 += 0.5
    elif saltoRana3 == 3:
        rana3 += 1
    elif saltoRana3 == 4:
        rana3 -= 0.5

print("\nla rana 1 avanzó: ",rana1)
print("la rana 2 avanzó: ",rana2)
print("la rana 3 avanzó: ",rana3)

if rana1 > rana2:
    if rana1 > rana3:
        print("La rana 1 avanzó mas.")
    else:
        print("La rana 3 avanzó mas.")
else:
    if rana2 > rana3:
        print("La rana 2 avanzó mas.")
    else:
        print("La rana 3 avanzó mas.")


