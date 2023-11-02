import sys

def ValidarEntero(mensaje):

    try:
        entero = int(input(mensaje))
    except ValueError as e:
        print("Valor erroneo, ingrese un número entero", file=sys.stderr)
        sys.exit()

    return entero

def ValidarReal(mensaje):

    try:
        real = float(input(mensaje))
    except ValueError as e:
        print("Error, ingrese un número real", file=sys.stderr)
        sys.exit()

    return real



