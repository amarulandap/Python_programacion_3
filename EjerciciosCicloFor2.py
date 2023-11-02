import ValidacionDeDatos


"""1. Encontrar al dato mayor de un conjunto ingresado desde el teclado"""

# Crear una lista para almacenar los datos ingresados desde el teclado.
datosComparacion = [ ]

while True:
    dato = ValidacionDeDatos.ValidarReal("Ingrese un número: ")

    datosComparacion.append(dato)
    print("Desea ingresar un nuevo valor:")
    print('\t 1. SI.')
    print('\t 2. NO.')
    nuevoValor= int(input(": "))


    if nuevoValor == 2:
        break;

# Recorrer la lista para encontrar el dato mayor.
datoMayor = datosComparacion[0]                     # Asumimos que el primer dato es el mayor.
for i in (datosComparacion):
    if i > datoMayor:                               # La variable i almacena cada uno de los valores de la lista.
        datoMayor = i

# Imprimir la lista
for i in (datosComparacion):
    print(i, end=" ")

# Imprimir el dato mayor.
print("\nEl dato mayor es: ", datoMayor)


"""2. Hallar los divisores enteros de un entero positivo"""

# Pedir que se ingrese un número entero.
print("\n")
while True:
    enteroDivisores = ValidacionDeDatos.ValidarEntero("Ingrese un número entero positivo: ")
    if enteroDivisores <= 0:                    # Validamos que sea un número positivo.
        print("Error.")
    else:
        break;

divisores = [ ]                                 # Creamos una lista para almacenar los divisores.
for i in range(1, enteroDivisores + 1):
    if enteroDivisores % i == 0:                # Con la operación modulo validamos el residuo de la división.
        divisores.append(i)                     # Agrego el divisor a la lista.

print("Divisores de: ", enteroDivisores)
for i in (divisores):                           # Imprimimos la lista de divisores enteros.
    print(i, end=" ")

# Para saber cuantos divisores enteros tiene el número.
cantidadDivisores = len(divisores)             # Calculamos el tamaño de la lista.
print("\nEl número ",enteroDivisores, "tiene", cantidadDivisores, "divisores")

# Para saber si el número es primo.
if cantidadDivisores > 2:
    print("El número", enteroDivisores, "no es primo.")       # Cada número tendrá como mínimo dos divisores.
else:
    print("El número", enteroDivisores, "es primo.")


"""3. Encontrar el equivalente en binario de un número entero positivo."""

# Pedir que se ingrese el número entero
print("\n")
while True:
    enteroDecimales = ValidacionDeDatos.ValidarEntero("Ingrese un número entero positivo: ")
    if enteroDecimales <= 0:                                  # Validamos que sea un número positivo.
        print("Error.")
    else:
        break;

EquivalenteBinario1 = bin(enteroDecimales)                   # Con la función bin hallamos el equivalente binario de un número entero.
print(EquivalenteBinario1)

b = ' '
while enteroDecimales > 0:
    EquivalenteBinario = enteroDecimales % 2                  # Almacenamos el residuo de cada división por 2.
    enteroDecimales = enteroDecimales // 2                    # Almacenamos el cociente de cada división por 2.
    b = str(EquivalenteBinario) + b

    print(b)














