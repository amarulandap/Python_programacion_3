from ValidacionDeDatos import *
from random import randint

"""1. Simular el lanzamiento de un dado y contar el número de veces que sale 3"""

lanzamientos = ValidarEntero("¿Cuantás veces desea lanzar el dado? ")       # Almacenamos el número de veces que se lanzará el dado.

numeroVeces = 0                                       # Variable para almacenar el número de veces que sale el 3.
resultadosLanzamiento = [ ]                           # Lista para almacenar los resultados de los lanzamientos del dado 1.

resultadosLanzamiento1 = [ ]                          # Almacenar los resultados del dado 2.
resultadosIguales = 0                                 # Almacenar los lanzamientos con resultados iguales.

while lanzamientos > 0:
    valorLanzado = randint (1, 6)               # Almacenamos el valor que sale en cada uno de los lanzamientos.
    valorLanzado1 = randint(1, 6)               # Dado 2.

    resultadosLanzamiento.append(valorLanzado)        # Listas para almacenar los resultados de los lanzamientos de ambos dados.
    resultadosLanzamiento1.append(valorLanzado1)

    if valorLanzado == 3:
        numeroVeces += 1                              # Acumulamos los lanzamientos donde sale el 3.

    lanzamientos -= 1

for i in (resultadosLanzamiento):                     # Imprimir la lista de resultados de los lanzamientos.
    print(i, end=" ")

print("Resultados favorables a 3: ", numeroVeces)

print("\n")
for i in (resultadosLanzamiento1):                   # Imprimir la lista de resultados de los lanzamientos del dado 2.
    print(i, end=" ")

for i in range (0, len(resultadosLanzamiento)):                # Las listas inician en la posición 0.
    if resultadosLanzamiento[i] == resultadosLanzamiento1[i]:
        resultadosIguales += 1

print("Número de lanzamientos iguales: ",resultadosIguales)


"""2. Uso del continue"""

listaPrueba = [1, 3, -5, 7, -9, 11, 13, -15, 17, 19, 21]
sumaPositivos = 0                                           # Acumular la suma de los números positivos.

for i in listaPrueba:
    if i < 0:
        continue
    else:
        sumaPositivos += i

print("La suma de los números positivos es: ",sumaPositivos)




















