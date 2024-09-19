"""
Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:
"""

while True:
    N = int(input("Introduce un entero positivo: "))
    if N > 0:
        break
    else:
        print("El número debe ser positivo. Por favor, intenta de nuevo.")

suma = N * (N + 1) / 2
print(f"La suma de todos los enteros desde 1 hasta {N} es: {suma}")

