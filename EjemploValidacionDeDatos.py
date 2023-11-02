# Solicitamos al usuario que ingrese la cantidad de datos a sumar.
# Con el bloque Try except controlamos el ingreso de datos erroneos.

""" try:
        cantidadDatos = int(input("Ingrese la cantidad de datos a sumar: "))
        datoCorrecto = True
    except ValueError:
        datoCorrecto = False

    if datoCorrecto == False:
        # Creamos la variable para almacenar la suma.
        print("Dato incorrecto, ingrese un número entero.")
        suma = 0
        cantidadDatos = 0

    else:
        suma = 0
"""

while True:
    try:
        cantidadDatos = int(input("Ingrese la cantidad de datos a sumar: "))
    except ValueError:
        print("Error.")
        continue                                        # Garantizo que se ejecute de nuevo el ciclo while.
    break                                               # Si el dato es correcto se interrumpe el ciclo.

# Creamos la variable para almacenar la suma.
suma = 0

# Crear el ciclo para realizar la suma.
contador = 0
while True:
    try:
        dato = int(input("sumando: "))          # Variable donde almacenamos los datos ingresados por el usuario.
    except ValueError:
        print("Error.")
        continue

    suma += dato
    contador += 1

    if contador == cantidadDatos:
        break

print("suma = ",suma)



