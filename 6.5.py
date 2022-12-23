"""
En una cancha juega el equipo A y el equipo B
diseñe un algoritmo que determine si ganó el equipo A, si ganó el equipo b 
o fue un empate 
"""
#declaración de variable
A = 0
B = 0

#entrada
A = float (input ("Ingrese los goles del equipo A: "))
B = float (input ("Ingrese los goles del equipo B: "))

#proceso
if A > B:
 print ("Ganó el equipo A!!!")
elif B > A:
 print ("Ganó el equipo B!!!")
else:
    print ("Fue un empate")
#salida