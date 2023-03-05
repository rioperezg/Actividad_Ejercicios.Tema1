"""""
Ejercicio 1
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre 
de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
"""
   
def Cadena(cadena):
    # Le damos la vuelta a la cadena para empezar
    Frase = cadena[::-1]
    # Separamos la cadena justo por la coma 
    Frase2 = Frase.split(",")
    nota = Frase2[0]
    Nombre_y_apellidos  = Frase2[1]
    # Devolvemos la cadena sin estar corrupta
    return "{} ha sacado un {}".format(Nombre_y_apellidos, nota)

