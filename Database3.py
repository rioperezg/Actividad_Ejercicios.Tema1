""""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse 
ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

"""
lista1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista2 = ["h",'o','l','a',' ', 'l','u','n','a']
def lista_final(lista_1,lista_2):
    Lista_final = []
    for i in lista_1:
        for j in lista_2:
            if i == j:
                Lista_final.append(i)
    print("En primera instancia la lista final es: ",Lista_final)
    Lista_final2 = []
    for Lista_final in Lista_final:
        if Lista_final not in Lista_final2:
            Lista_final2.append(Lista_final)
    return Lista_final2      
print(lista_final(lista1,lista2))