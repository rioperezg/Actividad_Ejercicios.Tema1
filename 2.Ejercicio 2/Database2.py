"""""
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""
numero_magico = 12345679
def operacion_num_mag():
    numero_usuario = input("introduzca un numero entre el 1 y el 9:")
    secondnum = numero_usuario*9
    return numero_magico*secondnum