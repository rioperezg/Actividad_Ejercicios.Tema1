"""
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el 
elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra 
en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.
Sugerencia
Puedes utilizar la sintaxis "elemento in lista"
elementos = [1, 5, -2]
"""
def agregar_una_vez(lista, el):
    if type(el) == list:
        # Dada la lista y el elemento, diferenciaremos si el elemento a añadir es de tipo lista o un unico elemento
        for i in el:
            if i not in lista:
                # Si es de tipo lista recorremos esta lista principal, y si i esta en la lista no añadimos i
                lista.append(i)
            else:
                print("Elemento:{}, in lista".format(i))
        return(lista, "Añadido varios elementos")               
    else:            
        if el not in lista:
            # Por el contrario si solo se añade un elemento simplemente se comprueba que no este en la lista principal
            lista.append(el)
        else:
            ValueError(print("Error: Imposible añadir elementos duplicados => [elemento]."))
        return(lista, "Añadido solo un elemento")
