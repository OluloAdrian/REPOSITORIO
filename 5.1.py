"""
Un alumno de ingenieria necesita sacar el promedio de sus 4 notas, 
diseña un algoritmo que promedie las 4 notas.
Para sacar el promedio se aplica la formula:
nota_1 + nota_2 + nota_3 +nota_4 / 4
"""
#Declaración de variables
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
promedio = 0.0

#Entrada
print ("Es momento de que ingreses las 4 notas")

nota1 = float (input ("ingrese la primera nota: "))
nota2 = float (input ("ingrese la segunda nota: "))
nota3 = float (input ("ingrese la tercera nota: "))
nota4 = float (input ("ingrese la cuarta nota: "))

#Proceso
promedio = nota1 + nota2 + nota3 + nota4
promedio = promedio/4.0

#Salida
print ("Su promedio es de: ", promedio)
print (f"Sus notas son: {nota1} , {nota2} , {nota3} , {nota4}")
