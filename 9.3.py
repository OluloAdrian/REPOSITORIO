"""
Una persona va de shopping, esta persona se comprará 4 prendas y ve un anuncio 
de un 10% por compras mayores a 170 soles, la necesita saber la suma de sus compras
para poder saber si tendrá un descuento o no.
diseñe un algoritmo que sume el precio de las prendas, si tendra 10% y de cuanto 
sería el descuento
"""

#declaracion de variables
suma = 0.0
ropa = 0.0
pago = 0.0
#entrada
#proceso

for x in range(4):
    ropa = float(input("Ingresa el precio de la prenda: "))
    suma = suma + ropa

if suma > 170:
 print ("Se lleva su descuentazo")
 descuentazo = 10/100 * suma
 print ("el descuento es de: ", descuentazo)
elif 170 >= suma:
 print ("No te llevas ningun descuento :3")
    
pago = suma - descuentazo
#salida
print("La suma de las prendas es de: " , suma)
print("El pago sería de: ",pago)