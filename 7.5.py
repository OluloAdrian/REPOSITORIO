"""
Dos equipos de basquet estan jugando un vs, leones contra cobras, diseña un algoritmo 
que determine si hubo un equipo ganador (Decir quien) o si hubo un empate 
"""
#declaración de variables
leones = 0
cobras = 0

#entrada
leones = int (input ("Ingrese las anotaciones de los leones: "))
cobras = int (input ("Ingrese las anotaciones de las cobras: "))

#proceso
if leones > cobras:
 print ("Ganaron los leones")
elif cobras > leones:
 print ("Ganaron las cobras")
else:
    print ("Es un Empate")