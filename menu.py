import Database1 as db1
import Database2 as db2
import Database3 as db3
import Database4 as db4
import Database5 as db5
import Database6 as db6
import Database7 as db7
import Formateo
def iniciar():
    opcion = int(input("Introduzca el numero del ejercicio que desea ejecutar:"))
    if opcion == 1:
        print("Ha seleccionado el ejercicio 1")
        Cadena = db1.nombre_y_apellidos(input("Introduzca la cadena que desea voltear:"))
        print(db1.nombre_y_apellidos.Cadena(self=Cadena))
    elif opcion == 2:
        print("Ha seleccionado el ejercicio 2")
        Num = db2.numero_final(input("Introduzca un numero entre el 1 y el 9:"))
        print(db2.numero_final.operacion(self=Num))
    elif opcion == 3:
        print("Ha seleccionado el ejercicio 3")
        lista_1 = input("Introduzca la primera lista:")
        lista_2 = input("Introduzca la segunda lista:")
        print(db3.lista_final(lista_1,lista_2)) 
    elif opcion == 4:
        print("Ha seleccionado el ejercicio 4")
        print(db4.ordenar(Tareas = Formateo.leerLista_pantalla(stri = input("Introduzca las Tareas a realizar:"))))
    elif opcion == 5:
        print("Ha seleccionado el ejercicio 5")
        number = input("Introduzca el numero a descomponer:")
        print(db5.Descomposicion(number))
    elif opcion == 6:
        print("Ha seleccionado el ejercicio 6")
        print(db6.Separar(Lista = Formateo.leerLista_nums(strr=input("Introduzca la lista de numeros:"))))
    elif opcion == 7:
        print("Ha seleccionado el ejercicio 7")
        print(db7.agregar_una_vez(lista = Formateo.leerLista_nums(strr=input("Introduzca la lista de num:")), el = Formateo.leerLista_nums(strr="Introduzca la lista de num:")))
        # Problema

    else:
        print("Solo se encuentran 7 ejercicios disponibles")
    pass                   

print(iniciar())