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
        for i in el:
            if i not in lista:
                lista.append(i)
            else:
                print("Elemento:{}, in lista".format(i))
        print(lista, "Añadido varios elementos")               
    else:            
        if el not in lista:
            lista.append(el)
        else:
            ValueError(print("Error: Imposible añadir elementos duplicados => [elemento]."))
        print(lista, "Añadido solo un elemento")
lista1 = [1, 2, 5, 6, 23, 2]  
print(agregar_una_vez(lista1, [3, 6, "hola"])) 