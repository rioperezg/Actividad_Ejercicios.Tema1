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
    if el == list:
        for el in el:
            if el not in lista:
                lista.append(el)
            else:
                pass
                ValueError(print("Error: Imposible añadir elementos duplicados => [elemento]."))
            break 
        print(lista)               
    else:            
        if el not in lista:
            lista.append(el)
        else:
            ValueError(print("Error: Imposible añadir elementos duplicados => [elemento]."))
        print(lista)
lista1 = [1, 2, 5, 6, 23, 2]  
print(agregar_una_vez(lista1, [3, 6, "hola"])) 