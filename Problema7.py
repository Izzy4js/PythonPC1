"""
Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

numero1 = float(input("Digita un número: "))
numero2 = float(input("Digita otro número: "))
seguir = True

while seguir:
    print("\nElige una opción:")
    print("1. Sumar los dos números")
    print("2. Restar los dos números")
    print("3. Multiplicar los dos números")
    print("4. Salir")

    opcion = input("\nDigita el número de la operacion que desea: ")
    if opcion == '1':
        suma = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {suma}")
    elif opcion == '2':
        resta = numero1 - numero2
        print(f"La resta de {numero1} y {numero2} es: {resta}")
    elif opcion == '3':
        multiplicacion = numero1 * numero2
        print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
    elif opcion == '4':
        print("Finalizado")
        seguir = False  # Cambia el valor de seguir para terminar el bucle
    else:
        print("Digite un número de nuestras opciones")
