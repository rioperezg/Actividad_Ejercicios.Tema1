"""""
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""
def operacion(numero_usuario):
    while True:
        # Hacemos que el numero sea entero por fuerza
        try:
            numero_usuario = int(numero_usuario)
        except:
            # Ademaas que este comprendido entre el 0 y el 10
            print("El numero no es valido")
        if 0 < numero_usuario < 10:
            break
        else:
            print("El numero se encuentra fuera del rango")
            pass
    # Y por ultimo realizamos todas las operaciones que se han especificado
    numero_magic = 12345679
    nuevo_num = numero_usuario*9
    print("El numero usuario :{}, multiplicado por 9 es: {}".format(numero_usuario, nuevo_num))
    numero_magico = nuevo_num * numero_magic
    # Devolvemos el numero final
    return "Finalmente, el numero que resulta de multiplicar {} y {} es: {}".format(numero_magic,nuevo_num, numero_magico)



