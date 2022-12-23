"""
Un profesor necesita contabilizar el partido de futbol de su salón,
diseñe un algoritmo que acumule los set de cada jugada, los goles de cada jugada 
y cuantos goles se hizo en total.
"""

#declaracion de variables
acu = 0.0
goles = 0
cont = 0

#entrada
#proceso
set = int (input("Cuantos sets se hicieron en total: "))

for x in range(set):
    goles = int(input("Ingresa los goles del set: "))
    acu = acu + goles
    cont = cont + 1
#salida
print("La acumulación de goles es de: " , acu)
print("Contador de cuantos sets ingresó: ", cont)