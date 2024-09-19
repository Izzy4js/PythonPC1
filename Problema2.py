"""
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
"""


comida = float(input("¿Cuánto fue el costo de tu comida en el restaurante? $"))
porcentaje = input("¿Qué porcentaje de propina deseas dejar?")

if '%' in porcentaje:
    porcentaje_propina = float(porcentaje.replace('%', ''))
else:
    porcentaje_propina = float(porcentaje)

if porcentaje_propina < 15:
    print("El porcentaje de propina debe ser al menos 15%. Se ajustará automáticamente a 15%.")
    porcentaje_propina = 15

propina = (comida * porcentaje_propina) / 100
print(f"La cantidad de propina que dejara es: ${propina:.2f}")


