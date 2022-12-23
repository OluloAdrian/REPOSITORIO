"""
Un profesor necesita sacar el promedio y la suma de las 5 notas de su alumno, 
diseña un algoritmo que promedie las 5 notas y las sume.

"""

#declaracion de variables
suma = 0.0
notas = 0.0

#entrada
#proceso
for x in range(5):
    notas = int(input("ingrese la nota: "))
    suma = suma + notas
    promedio = suma/5
    
#SI SEPARAS LA SUMA Y EL PROMEDIO DEL FOR, NO TE CONTARÁ LAS 5 NOTAS INGRESADAS
#SI DEJAS LA SUMA EN EL FOR SI TE CONTARÁ LAS 5 NOTAS

#salida
print("La suma es: " , suma)
print("El promedio es: " , promedio)