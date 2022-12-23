"""
Una persona colecciona FunkoPop y necesita saber
la suma de los 3 que se compró en diferentes lugares
"""

#declaracion de variables
suma = 0.0
funkos = 0.0

#entrada
#proceso

for x in range(3):
    funkos = float(input("Ingresa el costo del FunkoPop: "))
    suma = suma + funkos
    
#salida
print("La suma de los Funkos es de: " , suma)