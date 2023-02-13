
class nombre_y_apellidos:
    def __init__(self, cadena):
        self.cadena = cadena 
    @staticmethod      
    def Cadena(self):
        Frase = self.cadena[::-1]
        Frase2 = Frase.split(",")
        nota = Frase2[0]
        Nombre_y_apellidos  = Frase2[1]
        return "{} ha sacado un {}".format(Nombre_y_apellidos, nota)
        


        