"""
Un profesor necesita contabilizar el partido de voley de su salón,
diseñe un algoritmo que diga la cantidad de sets que se hicieron, la 
cantidad de puntos y que acumule los puntos totales.
"""

#declaracion de variables
acu = 0.0
puntos = 0
cont = 0

#entrada
#proceso
set = int (input("Cuantos sets se hicieron en total: "))

for x in range(set):
    puntos = int(input("Ingresa los puntos del set: "))
    acu = acu + puntos
    cont = cont + 1
#salida
print("La acumulación de puntos es de: " , acu)
print("Contador de cuantos sets ingresó: ", cont)