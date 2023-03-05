""""
Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce 
el número 3647:
python descomposicion.py 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
0007
0040
0600
3000
"""
from itertools import chain, product, repeat, cycle
def Descomposicion(num):
    numero = str(num)
    numero = list(numero)
    numero = numero[::-1]
    n = len(numero) - 1
    for i, letra in enumerate(numero):
        print("{}{}{}".format((n - i)*"0", letra, i*"0")) 
    return "Esta es la descomposicion de {}".format(num)
# print(Descomposicion(123678))