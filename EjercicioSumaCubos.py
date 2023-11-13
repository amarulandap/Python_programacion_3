"""Calcular la suma de 1**3 + 2**3 + 3**3 + ........ +n**3"""

# Solicitar un número natural.
# Crear una variable para almacenar la suma.
# Calcular la serie.
# Mostrar el resultado en pantalla.

from ValidacionDeDatos import *
from math import *

while True:
    numero = ValidarEntero("Ingrese un número mayor que cero: ")

    if numero > 0:
        break

sumaCubos = 0
for i in range (1, numero + 1):
    sumaCubos += pow(i, 3)

print("Suma = ",sumaCubos)



"""Calcular el pago anual y total por la compra de una maquina."""

# Precio de la máquina $20.000.000 (P).
# Número de años 5 (n).
# interés anual (r). (0.01, 0.02, 0.1, 0.2,...)
# Pago anual.
# pago total.

# Solicitar el precio de venta de la máquina.
# Solicitar la tasa de interés.
# Solicitar la duración del crédito. Es decir, el número de años.
# Calcular el pago anual. (recordar dividir la tasa por 100)
# Calcular el pago total.

precioMaquina = ValidarEntero("\nIngrese el precio de la máquina(sin comas ni puntos, solo los dígitos): ")
numeroAnios = ValidarEntero("Ingrese el número de años del crédito: ")

interes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for j in range (0, len(interes)):

    tasaInteres = interes[j]

    denominador = pow(1 + tasaInteres / 100, numeroAnios) - 1
    numerador = (tasaInteres / 100) * pow(1 + tasaInteres / 100, numeroAnios)

    pagoAnual = precioMaquina * (numerador / denominador)

    pagoTotal = pagoAnual * numeroAnios

    print("\nPago anual = $",format(pagoAnual, ".3f"), "Pago total: $",format(pagoTotal, ".3f"), "Tasa interés: ", tasaInteres,"%")








