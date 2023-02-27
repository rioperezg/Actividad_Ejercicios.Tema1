"""""
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""
#necesitamos proporcionar un programa que dado un numero entre el 1 y el 9 haga dichas operaciones ademas forzaremos a que el programa
#obligue introducir dicho numero con esos parametros
#Empecemos por el numero_usuario
class numero_final:
    def __init__(self, numero_usuario):
        self.numero_usuario = numero_usuario
        while True:
            try:
                self.numero_usuario = int(self.numero_usuario)
            except:
                print("El numero no es valido")
            if 0 < self.numero_usuario < 10:
                break
            else:
                print("El numero se encuentra fuera del rango")
                pass
    def operacion(self):
        numero_magic = 12345679
        nuevo_num = self.numero_usuario*9
        print("El numero usuario :{}, multiplicado por 9 es: {}".format(self.numero_usuario, nuevo_num))
        numero_magico = nuevo_num * numero_magic
        return "Finalmente, el numero que resulta de multiplicar {} y {} es: {}".format(numero_magic,nuevo_num, numero_magico)

P = numero_final(input("Introduzca un numero entre el 1 y el 9:"))
print(P.operacion())


