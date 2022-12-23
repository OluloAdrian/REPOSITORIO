"""
Una persona necesita sacar la suma de los ahorros 
que tuvo en los ultimos 4 meses 
diseña un algoritmo que sume los ahorros de los 4 meses.
"""

#declaracion de variables
suma = 0.0
ahorros = 0.0

#entrada
#proceso

for x in range(4):
    ahorros = float(input("Ingresa el ahorro: "))
    suma = suma + ahorros
    
#salida
print("La suma de los ahorros es de: " , suma)