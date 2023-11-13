"""calcular el descuento de una compra hecha en un supermercado."""

# Total de la compra.
# Número al azar.
# Descuento.
# Total a pagar.

# Solicitar el valor total de la compra.
# Generar el número al azar.
# Calcular el descuento con base en el número generado.
# Calcular el total a pagar.
# Mostrar en pantalla el descuento y el total a pagar.

from ValidacionDeDatos import *
from random import *

totalCompra = ValidarEntero("Total compra: $ ")

numeroAzar = randint(5, 9)

if numeroAzar < 7:
    descuento = totalCompra * 0.05
else:
    descuento = totalCompra * 0.10

totalAPagar = totalCompra - descuento

print("Número = ",numeroAzar)
print("Descuento = $ ",descuento)
print("Total a pagar = $ ",totalAPagar)


"""Mostrar dos números aleatorios cuya suma sea un número primo"""



