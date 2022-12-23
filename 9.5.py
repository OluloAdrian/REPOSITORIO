"""
Un profesor necesita sacar el promedio y la suma las edades de sus 10 alumnos, 
diseña un algoritmo que promedie las 10 edades y las sume.
"""

#declaracion de variables
suma = 0
edades = 0.0

#entrada
#proceso
for x in range(10):
    edades = int(input("ingrese la edad: "))
    suma = suma + edades
    promedio = suma/10
    
#salida
print("La suma de las edades es: " , suma)
print("El promedio de las edades es: " , promedio)