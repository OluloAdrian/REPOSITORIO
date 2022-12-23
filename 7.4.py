"""
Un niño va de compras, si todo le sale más de 100 soles, recibe un descuento del 20%,
si sale menos, no se lleva nada, diseñe un algoritmo que determine 
si el niño tendra un descuento y si es así de cuanto sería.
"""

#declaración de variables
compras = 0.0
descuentazo = 0.0

#entrada
compras = float (input ("Ingrese lo que gastó en compras: "))

#proceso
if compras > 100:
 print ("Se lleva su descuentazo")
 descuentazo = 20/100 * compras
 print ("el descuento es de: ", descuentazo)
elif 100 >= compras:
 print ("No te llevas nada :3")

#salida
