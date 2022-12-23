"""
Realice un algoritmo que permita calcular el volumen de un 
cilindro ingresando el valor de el radio (r) y la altura (h). Considera
la siguiente formula
v =  π x r² x h
"""
#Declaracion de variables
r = 0.0
h = 0.0
v = 0.0

#Entrada
r = float (input ("ingrese el radio: "))
h = float (input ("ingrese la altura: "))

#Proceso
v =  3.1416 * r * r * h

#Salida
print ("El volumen del cilindro es: ", v)