"""
Diseña un algoritmo en el que se ingrese 2 digitos para restarlos
y el programa los contabilice y los acumule usando el while.
"""
#declaracion de variables
acu = 0 
cont = 0
resta = 0
#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    acu = acu + num1 + num2
    cont = cont + 2
    resta = num1 - num2
    print ("La resta es: ", resta)
    print("La acumulación de resta es de: " , acu)
    print("Contador de cuantos digitos ingresó: ", cont)

    rpt = str (input ("Desea realizar otra resta? si/no : "))