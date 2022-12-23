"""
Un profesor necesita contabilizar el partido de basquet de su salón,
diseñe un algoritmo que diga la cantidad de sets que se hicieron, la 
cantidad de anotaciones y que acumule las anotaciones totales.
"""

#declaracion de variables
acu = 0.0
anotaciones = 0
cont = 0

#entrada
#proceso
set = int (input("Cuantos sets se hicieron en total: "))

for x in range(set):
    anotaciones = int(input("Ingresa las anotaciones del set: "))
    acu = acu + anotaciones
    cont = cont + 1
#salida
print("La acumulación de anotaciones es de: " , acu)
print("Contador de cuantas sets ingresó: ", cont)