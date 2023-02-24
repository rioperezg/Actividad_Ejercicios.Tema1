"""
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera 
con los números pares y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]
[1, 5, 7]
"""
def Separar(Lista):
    Pares = []
    Impares = []
    for i in Lista:
        if i % 2:
            Impares.append(i)
        else:
            Pares.append(i)
    return ("Estos son los numeros pares: {}, y estos son los numeros impares: {}".format(Pares, Impares))
# print(Separar([23,42,56,18,35,76,81]))
    
    