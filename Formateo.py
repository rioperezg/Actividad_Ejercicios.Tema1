# El objetivo de este archivo.py es el de transformar las cadenas introducidas por pantalla mediante el metodo input, en listas.
# Ya que no hay forma de introducir listas con el metodo input.
def leerLista_pantalla(strr):
    lista_nums =[]
    # Los elementos de las listas han de ser introducidos y separados por comas, por lo que en esta funcion separamos la cadena 
    # introducida justo donde se encuentra la coma.
    strr = strr.split(",")
    for i in strr:
        try:
            # Por otro lado, recorremos esta lista, y probamos si el elemento es entero, en tal caso lo añadimos a la lista vacia, 
            # y si no se puede transformar en entero lo dejamos como str y lo añadimos a la lista vacia
            i = int(i)
        except:
            pass
            i = str(i)   
            lista_nums.append(i)
        else:
            i = int(i)
            lista_nums.append(i)    
    return lista_nums
