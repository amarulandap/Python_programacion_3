from math import *
import ValidacionDeDatos

"""1. Secuencia controlada por una lista"""

for i in [1,2,3,4,5,6,7,8,9]:
    cuadrado = pow(i, 2)

    print(i, cuadrado)

ciudades = ['Medellin', 'Cali', 'Bogotá', 'Pasto', 'Barranquilla', 'Armenia']

print('\n')
for i in (ciudades):
    print(i, end=", ")


"""2. Secuencia definida mediante un rango"""

print('\n')
for i in range(11):                 # El valor inicial siempre será cero. No se incluye el limite superior.
    print(i, end=" ")

print('\n')
for i in range(10, 20):            # El extremo inferior siempre debe ser un número menor.
    print(i, end=" ")

print('\n')
for i in range(20, 40, 2):         # Especificando el incremento que deseamos.
    print(i, end=" ")


"""3. Calcular la suma de los cuadrados primeros n números naturales"""

print('\n')
cantidadNaturales = ValidacionDeDatos.ValidarEntero("Ingrese la cantidad de números naturales: ")   # Pedimos la cantidad de números naturales a sumar.

sumaNaturales = 0               # Creamos la variable para almacenar la suma.

for natural in range(1, cantidadNaturales + 1):
    cuadradoNatural = pow(natural, 2)       # calculamos el cuadrado de cada número natural.

    sumaNaturales += cuadradoNatural            # Acumulamos la suma de cada uno de los cuadrados.

print("El valor de la suma es =", sumaNaturales)


"""4. Calcular el promedio de un grupo de datos ingresado desde el teclado. """

print('\n')
# Pedimos la cantidad de datos que se desea promediar.
cantidadNumeros = ValidacionDeDatos.ValidarEntero("Ingrese la cantidad de datos a promediar: ")

# Crear una lista para almacenar los datos ingresados desde el teclado.
listaNumerosPromedio = [ ]

# Ingresamos los datos en la lista.
for i in range(cantidadNumeros):                         # Recordemos que las listas inician en la posición 0.
    dato = ValidacionDeDatos.ValidarEntero("Ingrese un dato entero: ")
    listaNumerosPromedio.append(dato)

# Crear una variable para almacenar la suma de los datos.
sumaPromedio = 0

for i in (listaNumerosPromedio):
    sumaPromedio += i                                    # Recorrer los datos de la lista con la variable i.

promedio = sumaPromedio / cantidadNumeros
print("El promedio es:", promedio)


"""5. Verificar que la suma de los primeros n números impares, es igual al cuadrado de n"""

# Pedir el valor de los n números.
print('\n')
numerosImpares = ValidacionDeDatos.ValidarEntero("Ingrese la cantidad de números impares: ")

sumaNumerosImpares = 0                                   # Almacenar la sumatoria de los números impares.
for i in range(1, 2 * numerosImpares + 1, 2):
    sumaNumerosImpares += i

cuadradoNumerosImpares = pow(numerosImpares, 2)      # calcular el cuadrado de la cantidad de números impares.

if (sumaNumerosImpares == cuadradoNumerosImpares):
    print(sumaNumerosImpares, " = ", cuadradoNumerosImpares)
else:
    print(sumaNumerosImpares, " != ", cuadradoNumerosImpares)












