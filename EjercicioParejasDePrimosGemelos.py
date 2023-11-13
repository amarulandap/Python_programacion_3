"""Generar n parejas de números primos gemelos."""

# numero de parejas.
# parejas de número primos.

# Solicitar la cantidad de parejas a generar.
# crear un ciclo que se repita hasta generar las parejas ingresadas.
# Generar dos números aleatorios.
# Validar si ambos son número primos.
# Validar que la distancia entre ellos es dos.
# Mostrar las parejas de números primos.

from ValidacionDeDatos import ValidarEntero
from ValidacionDeDatos import ValidarReal
from random import randint
from math import pow

numeroParejas = ValidarEntero("Ingrese el número de parejas a generar: ")       # Pidiendo el número de parejas.

parejasGeneradas = 0                                # Acumular el número de parejas que se van generando.
DivisoresNumero1 = [ ]                              # Almacenar los divisores de cada número.
DivisoresNumero2 = [ ]
contadorIntentos = 0                                # Limitar el número de iteraciones del ciclo.
while True:

    numero1 = randint(1, 20)              # Números entre 1 y 20 generados al azar.
    numero2 = randint(1, 20)
    contadorIntentos += 1

    for i in range (1, numero1 + 1):                # Validando si el número 1 es primo.
        if numero1 % i == 0:
            DivisoresNumero1.append(i)

    if len(DivisoresNumero1) == 2:                  # Si el numero1 es primo, generamos el segundo.
        for j in range(1, numero2 + 1):             # Validando si el número 2 es primo.
            if numero2 % j == 0:
                DivisoresNumero2.append(j)

        if len(DivisoresNumero2) == 2:              # Si ambos números son primos.
            if numero1 - numero2 == 2 or numero1 - numero2 == -2:
                parejasGeneradas += 1
                print(numero1, " y ", numero2, " son números primos gemelos.")

    if parejasGeneradas == numeroParejas or contadorIntentos == 20:           # Condición que interrumpe la ejecución del ciclo.
        break


""" Interpretar un algortimo"""

# Ingresar dos números num1 y num2.
num1 = ValidarReal("\nIngrese el primer número: ")
num2 = ValidarReal("Ingrese el segundo número: ")

# Inicializar un avariable acumuladora.
acum = 0

if num1 < 5:
    acum += (num1 - num2)

print("Acumulador = ",acum)


"""Cambiar un ciclo for por un ciclo while"""

limiteSuperior = ValidarEntero("\nIngrese un número > 1: ")               # Pedimos que se ingrese el dato del límite superior.

potencia = 0                                                            # Acumulador de potencias.

contador = 0                                                            # Contador para control del ciclo.
while contador <= limiteSuperior:

    potencia += pow(contador, 2)
    contador += 1

print("Potencia = ",potencia)





