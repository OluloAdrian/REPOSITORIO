"""
Diseña un algoritmo en el que se halle un lado del triangulo, 
ingresando los otros 2 lados. Mediante la ley de coseno.
"""
#declaracion de variables
acu = 0 
cont = 0
z = 0
Pi = 3.1416
import math
#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    a = float (input ("ingrese el primer lado: "))
    b = float (input ("ingrese el segundo lado: "))
    alfa = float (input ("ingrese el ángulo en grados sexagesimales: "))
    acu = acu + a + b
    cont = cont + 2
    z = (a**2 + b**2 - 2*a*b*math.cos(alfa*Pi/180))**0.5
    print ("El lado es ", z)
    print("La acumulación de lados es: " , acu)
    print("Contador de cuantos digitos ingresó: ", cont)

    rpt = str (input ("Desea realizar otra resta? si/no : "))