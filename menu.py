import Database1 as db1
import Database2 as db2
# import Database3 as db3
# import Database4 as db4
# import Database5 as db5
# import Database6 as db6
# import Database7 as db7
def iniciar():
    opcion = int(input("Introduzca el numero del ejercicio que desea ejecutar:"))
    if opcion == 1:
        print("Ha seleccionado el ejercicio 1")
        P = db1.nombre_y_apellidos(input("Introduzca la cadena que desea voltear:"))
        print(db1.nombre_y_apellidos.Cadena(self=P))
    elif opcion == 2:
        print("Ha seleccionado el ejercicio 2")
        Q = db2.numero_final(input("Introduzca un numero entre el 1 y el 9:"))
        print(db2.numero_final.operacion(self=Q))
    elif opcion == 3:
        print("Ha seleccionado el ejercicio 3")
        
    elif opcion == 4:
        print("Ha seleccionado el ejercicio 4")
    elif opcion == 5:
        print("Ha seleccionado el ejercicio 5")
    elif opcion == 6:
        print("Ha seleccionado el ejercicio 6")
    elif opcion == 7:
        print("Ha seleccionado el ejercicio 7")
    else:
        print("Solo se encuentran 7 ejercicios disponibles")                   

print(iniciar())