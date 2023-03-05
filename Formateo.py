
def leerLista_pantalla(strr):
    lista_nums =[]
    strr = strr.split(",")
    for i in strr:
        try:
            i = int(i)
        except:
            pass
            i = str(i)   
            lista_nums.append(i)
        else:
            i = int(i)
            lista_nums.append(i)    
    return lista_nums
# print(leerLista_pantalla("2,3,hola"))