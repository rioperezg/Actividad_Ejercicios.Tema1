import sys
def leerLista_pantalla(stri):
    cadena = stri.split(",")
    return cadena
# print(leerLista_pantalla("2Hacer la comida,3limpiar la casa,1hacer la cama"))
# print(leerLista_pantalla("2,3,4,56,76"))
def leerLista_nums(strr):
    lista_nums =[]
    strr = strr.split(",")
    for i in strr:
        i = int(i)
        lista_nums.append(i)
    return lista_nums
print(leerLista_nums("2,3,6"))    

def leerLista_nums(strr):
    lista_nums =[]
    strr = strr.split(",")
    for i in strr:
        try:
           i = int(i)
        except:       
           lista_nums.append(i), file = sys.stderr
        else:
            break
        sys.exit   
    return lista_nums
"""
import sys
def num():
    while True:
        numeros = input("valor: ")
        try: 
            numeros = int(numeros)
        except:
            print("valor no aceptado", file=sys.stderr)
        else:
            break
        sys.exit
    return str(numeros)
def Descomponer():
    numeros = num()
    numero = numeros[::-1]
    ceros_izquierda = 0
    while True:
        for i in str(numero):
            ceros_izquierda+=1
            print((i.ljust(int(ceros_izquierda), "0")).zfill(len(numero)), "\n")
            #l.just: left justified
            #.zfill:Pad a numeric string with zeros on the left, to fill a field of the given width.
        if ceros_izquierda >= len(numero):
"""