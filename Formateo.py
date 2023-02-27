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
# print(leerLista_nums("2,3,hola"))    
