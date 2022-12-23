"""
Diseña un algoritmo en el que se ingrese 2 digitos para dividirlos
y el programa los contabilice y los acumule usando el while.
"""
#declaracion de variables
acu = 0 
cont = 0
div = 0
#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    acu = acu + num1 + num2
    cont = cont + 2
    div = num1 // num2
    print ("La divición es: ", div)
    print("La acumulación de la división es de: " , acu)
    print("Contador de cuantos digitos ingresó: ", cont)

    rpt = str (input ("Desea realizar otra división? si/no : "))