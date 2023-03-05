""""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse 
ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

"""

def lista_final(lista_1,lista_2):
    Lista_final = []
    for i in lista_1:
        for j in lista_2:
            # Recorremos las dos listas introducidas y si hay algun elemento en comun, añadimos el elemento a lista vacia
            if i == j:
                Lista_final.append(i)
    print("En primera instancia la lista final es: ",Lista_final)
    Lista_final2 = []
    for Lista_final in Lista_final:
        # Mas tarde recorremos esta lista y añadimos todos los elementos que no se encuentren en la lista vacia 2 de modo que cuando 
        # se repitan no se añadiran
        if Lista_final not in Lista_final2:
            Lista_final2.append(Lista_final)
    return Lista_final2      
