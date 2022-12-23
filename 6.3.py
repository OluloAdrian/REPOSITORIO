"""
Diseñe un algoritmo en el que una persona pueda saber 
en que etapa de desarrollo se encuentra según su edad
"""
#declaración de variables
edad = 0

#entrada
edad = float (input ("Ingrese la edad: "))

#proceso
if 0<= edad and 5 >= edad:
    print ("Usted se encuentra en la infancia!")
elif 6<= edad and 11>= edad:
    print ("Usted se encuentra en la niñez!")
elif 12<= edad and 17 >= edad:
    print ("Usted se encuentra en la adolescencia")
elif 18<= edad and 24 >= edad:
    print ("Usted se encuentra en la juventud")
elif 25<= edad and 60 >= edad:
    print ("Usted se encuentra en la adultez")
elif 61<= edad and 94 >= edad:
    print ("usted se encuentra en la vejez")
else:
    print ("Sigues vivo???")

#salida