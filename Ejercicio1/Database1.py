"""""
Ejercicio 1
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre 
de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
"""
#Creamos una clase para recibir dicha cadena corrupta y poder transformalo en una cadena legible.
class nombre_y_apellidos:
    #A continucaion creamos el constructor de la clase, que se va a componer unicamente de cadena, ya que es solo la cadena corrupta.
    def __init__(self, cadena):
        self.cadena = cadena 
    @staticmethod      
    def Cadena(self):
        Frase = self.cadena[::-1]
        Frase2 = Frase.split(",")
        nota = Frase2[0]
        Nombre_y_apellidos  = Frase2[1]
        return "{} ha sacado un {}".format(Nombre_y_apellidos, nota)
cadena1 = nombre_y_apellidos("zereP nauJ,01")
cadena1.Cadena()