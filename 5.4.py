"""
Diseñe un algoritmo que determine el área (A) y el volumen (v) de una esfera 
de la que se conoce su radio (r). Considere las siguientes fórmulas:
A = 12.57 x r² 
V = (12.57 x r²)/3
"""

#declaración de variables
A = 0.0
V = 0.0
r = 0.0

#entrada
r = float (input ("ingrese el radio: "))

#proceso
A = 12.57 * r * r
V = (12.57 * r * r)/3

#salida
print ("El volumen del cilindro es: ", V)
print ("El área del cilindro es: ", A)