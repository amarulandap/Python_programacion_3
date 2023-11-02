from math import *
from ValidacionDeDatos import *
from random import *

"""1. Generar todas las parejas de números entre 1 y 3"""

for a in range(1, 4):
    for b in range(1,4):
        print(a, b)


"""2. Listar todas las parejas de números de 1 a 3, pero sin repetir parejas."""

print('\n')
for a in range(1, 4):
    for b in range(a, 4):
        print(a, b)


"""3. Para cada mes, mostrar una lista numerada de las 4 semanas"""

print('\n')
listaMeses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
listaSemanas = ['Semana1', 'Semana2', 'Semana3', 'Semana4']

for mes in listaMeses:
    print('Mes:', mes)
    for semana in listaSemanas:
        print(semana)


"""4. Lista de todas las ternas de números entre 1 y 20 que cumplen con la propiedad de i**2 + j**2 = k**2"""

print('\n')
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):

            if(pow(i, 2) + pow(j, 2) == pow(k, 2)):
                print(i,"^ 2 + ",j,"^ 2 = ",k,"^ 2")

# Si deseamos que no se impriman las ternas repetidas, debemos iniciar los dos ciclos interiores en i y j respectivamente.
# for j in range(i, 21);
# for k in range(j, 21);


"""5. Demostrar que una expresión lógica es una tautología"""

# Una tautología corresponde a una tabla de verdad cuyos resultados son todos verdaderos.
print('\n')
print("a    b    c    p")

# !(a and b) or (a or c).
for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            p = not(a and b) or (a or c)

            print(a, b, c, p)

"""6. Validar que dos números son amigables"""

print('\n')
numero1 = ValidarEntero("Ingrese el primer número: ")           # Números a validar.
numero2 = ValidarEntero("Ingrese el segundo número: ")

sumaDivisores1 = 0                                              # Acumuladores de los divisores de los números.
sumaDivisores2 = 0

for i in range(1, numero1 + 1):
    if numero1 % i == 0:
        sumaDivisores1 += i

for j in range(1, numero2 + 1):
    if numero2 % j == 0:
        sumaDivisores2 += j

if sumaDivisores1 == sumaDivisores2:
    print("Los números ",numero1, "y", numero2, "son números amigables.")
else:
    print("Los números ", numero1, "y", numero2, "no son números amigables.")


"""7. Interrupción usando la instrucción break"""

print('\n')
intentos = 0
while True:
    valorDado = randint(1, 6)

    if valorDado == 5:
        break;
    else:
        intentos += 1

print("Número intentos: ",intentos)




