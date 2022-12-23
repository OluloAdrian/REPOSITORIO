"""
Diseña un algoritmo que determine el Perimetro (P) y el Área (A) de un rectangulo 
del que se conoce su base (b) y su altura (h). Considera las siguientes formulas:
P = 2 x (b + h)
A = b x h
"""
#Declaracion de variables
b = 0.0
h = 0.0
P = 0.0
A = 0.0

#Entrada
b = float (input ("ingrese la base: "))
h = float (input ("ingrese la altura: "))

#Proceso
P = 2 * (b + h)
A = b * h

#Salida
print (f"El perimetro del rectangulo es {P} y el área es {A}")
