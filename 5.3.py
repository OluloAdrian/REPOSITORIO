"""
Juan quiere repartir un monto a sus 5 hijos, cada uno recibira una
parte equivalente a:
- Adrian: 25% del monto. 
- Brayan: 45% del monto recibido por Carl. 
- Carl: 35% de la monto. 
- Diana: 40% del monto recibido por Adrian.
- Efrain: lo que queda de la donación. 
Dado el importe del monto, diseñe un algoritmo que determine qué 
cantidad de dinero le corresponde a hijo.
"""
#declaracion de variables
monto = 0.0
a = 0.0
c = 0.0
b = 0.0
d = 0.0
e = 0.0

#entrada
monto = float (input ("ingrese la donación: "))

#proceso
a = 25/100*monto
c = 35/100*monto
b = 45/100*c
d = 40/100*a
e = monto-a-c-b-d

#salida
print ("Donación para Adrian: ", a )
print ("Donación para Carl : ", c )
print ("Donación para Brayan : ", b )
print ("Donación para Diana : ", d )
print ("Donación para Efrain: ",e )
