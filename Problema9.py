"""
Problema 9:
Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di'].
"""

palabras = input("Introduce las palabras para la lista, separadas por espacios: ")

lista = palabras.split()

lista_invertida = lista[::-1]
print("Lista invertida:", lista_invertida)

