"""hallar el MCD de dos números enteros"""

# Variables de entrada
# numero1, numero2      Números enteros a validar.

# Variables de salida
# maxComunDiv de ambos números.

# Procesos
# Solicitar ambos números.
# Crear dos listas para almacenar los divisores de ambos números.
# Crear una lista para los divisores comunes.
# Hallar los divisores y agregarlos a las listas.
# Hallar los divisores en común.
# Hallar el elemento mayor en la lista.
# Mostrar el resultado en pantalla.

from ValidacionDeDatos import *

numero1 = ValidarEntero("Ingrese el primer número: ")
numero2 = ValidarEntero("Ingrese el segundo número: ")

listaNumero1 = [ ]
listaNumero2 = [ ]
listaComunes = [ ]

for i in range(1, numero1 + 1):
    if numero1 % i == 0:
        listaNumero1.append(i)

for j in range(1, numero2 + 1):
    if numero2 % j == 0:
        listaNumero2.append(j)

for i in listaNumero1:
    for j in listaNumero2:
        if i == j:
            listaComunes.append(j)

maxComunDiv = listaComunes[0]
for i in listaComunes:
    if i > maxComunDiv:
        maxComunDiv = i

print("El MCD de ", numero1, " y ",numero2, " es ", maxComunDiv)


