"""
Un profesor necesita sacar la acumulacion de la edad de sus alumnos,
diseñe un algoritmo que acumule las edades ingresadas y que 
digite cuantos se ingresaron.

"""

#declaracion de variables
acu = 0.0
alumnos = 0.0
cont = 0

#entrada
#proceso
cantidad = int (input("Cuantas edades desea ingresar: "))

for x in range(cantidad):
    alumnos = float(input("Ingresa la edad del alumno: "))
    acu = acu + alumnos
    cont = cont + 1
#salida
print("La acumulación de la edad de los alumnos es de:"  , acu)
print("Contador de cuantas edades ingresó: ", cont)