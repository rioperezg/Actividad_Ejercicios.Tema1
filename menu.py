import Ejercicio_1 as E1
import Ejercicio_2 as E2
import Ejercicio_3 as E3
import Ejercicio_4 as E4
import Descomposicion as db5
import Ejercicio_6 as E6
import Ejercicio_7 as E7
import Formateo
def iniciar():
    opcion = int(input("Introduzca el numero del ejercicio que desea ejecutar:"))
    if opcion == 1:
        print("Ha seleccionado el ejercicio 1")
        Cadena = input("Introduzca la cadena que desea voltear:")
        print(E1.Cadena(Cadena))
    elif opcion == 2:
        print("Ha seleccionado el ejercicio 2")
        Num = input("Introduzca un numero entre el 1 y el 9:")
        print(E2.operacion(Num))
    elif opcion == 3:
        print("Ha seleccionado el ejercicio 3")
        lista_1 = input("Introduzca la primera lista:")
        lista_2 = input("Introduzca la segunda lista:")
        print(E3.lista_final(lista_1,lista_2)) 
    elif opcion == 4:
        print("Ha seleccionado el ejercicio 4")
        print(E4.ordenar(Tareas = Formateo.leerLista_pantalla(strr = input("Introduzca las Tareas a realizar:"))))
    elif opcion == 5:
        print("Ha seleccionado el ejercicio 5")
        number = input("Introduzca el numero a descomponer:")
        print(db5.Descomposicion(number))
    elif opcion == 6:
        print("Ha seleccionado el ejercicio 6")
        print(E6.Separar(Lista = Formateo.leerLista_pantalla(strr=input("Introduzca la lista de numeros:"))))
    elif opcion == 7:
        print("Ha seleccionado el ejercicio 7")
        print(E7.agregar_una_vez(lista=Formateo.leerLista_pantalla(strr = input("Introduzca la lista:")), el=Formateo.leerLista_pantalla(strr = input("Introduzca los elementos a añadir:"))))
    else:
        print("Solo se encuentran 7 ejercicios disponibles")
    pass
                       

print(iniciar())