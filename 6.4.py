"""
diseñe un algoritmo que determine si el alumno aprobó o desaprobó el curso, 
la nota minima para aprobar es de 10.5
"""
#declaración de variable
nota = 0.0

#entrada
nota = float (input ("Ingrese la nota del estudiante: "))

#proceso
if nota > 10.4:
 print ("Aprobaste")
else:
    print ("Desaprobaste")
#salida