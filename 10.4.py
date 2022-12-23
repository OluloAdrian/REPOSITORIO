"""
Una persona necesita sacar la acumulación de los ahorros que tuvo,
diseñe un algoritmo que acumule los ahorros ingresados y que 
digite cuantos se ingresaron.

"""

#declaracion de variables
acu = 0.0
ahorros = 0.0
cont = 0

#entrada
#proceso
cantidad = int (input("Cuantos ahorros desea ingresar: "))

for x in range(cantidad):
    ahorros = float(input("Ingresa el ahorro: "))
    acu = acu + ahorros
    cont = cont + 1
#salida
print("La acumulación de los ahorros es de: " , acu)
print("Contador de cuantos ahorros ingresó: ", cont)