"""
Dos niñas juegan a saltar la cuerda, la niña que salte más veces gana, 
diseña un algoritmo que determine que niña ganó o si fue un empate, 
si se tiene que insertar por teclado el numero de veces que cada niña salto la cuerda.
"""
#declaración de variables
niña1 = 0
niña2 = 0

#entrada
niña1 = int (input ("Ingrese cuantas veces salto la cuerda la primera niña: "))
niña2 = int (input ("Ingrese cuantas veces salto la cuerda la segunda niña: "))

#proceso
if niña1 > niña2:
 print ("Ganó la primera niña")
elif niña2 > niña1:
 print ("Ganó la segunda niña")
else:
    print ("Empate")


#salida




 

