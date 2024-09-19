""""
Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""

peso_payaso = 112
peso_muñeca = 75

num_payasos = int(input("¿Cuántos payasos se vendieron en el último pedido? "))
num_muñecas = int(input("¿Cuántas muñecas se vendieron en el último pedido? "))

peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
print(f"El peso total del paquete es: {peso_total} gramos")
