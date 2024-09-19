"""
Problema 8:
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""

hora = input("Introduce la hora en formato 24 horas (HH:MM): ")

horas, minutos = hora.split(':')
horas = int(horas)
minutos = int(minutos)

if (horas == 7 and 0 <= minutos <= 59) or (horas == 8 and minutos == 0):
    print("Es la hora del desayuno.")
elif (horas == 12 and 0 <= minutos <= 59) or (horas == 13 and minutos == 0):
    print("Es la hora del almuerzo.")
elif (horas == 18 and 0 <= minutos <= 59) or (horas == 19 and minutos == 0):
    print("Es la hora de la cena.")
else:
    pass
