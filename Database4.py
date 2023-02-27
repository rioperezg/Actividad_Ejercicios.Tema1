""""
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un 
orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""
#Mi idea es predefinir un diccionario con el orden ya establecido. Y con el metodo sort ordenar todas las tareas de mayor a menor 
#importancia de acuerdo al numero que estan asignados. no, tenemos que hacerlo de forma diferente
Tareas_domesticas = ["2Hacer la comida", "3limpiar la casa", "1hacer la cama"]
# Tareas_domesticas.sort()
# print(Tareas_domesticas)
import Formateo
def ordenar(Tareas = Formateo.leerLista_pantalla(stri = input("Introduzca las Tareas a realizar:"))):
    Tareas_ordenadas = [] 
    Tareas.sort()
    for indice, i in enumerate(Tareas):
        i = list(i)
        # print("Tarea",[indice + 1],":{}".format(i))
        for j in i:
            if j == indice:
                i.append(j)
            else:
                i.remove(j)
                print("Tarea",[indice + 1],i)          
                break
        i = "".join(i)
        Tareas_ordenadas.append(i)
    return Tareas_ordenadas
    
        
              
# print(ordenar(Tareas_domesticas))   

""""
PRUEBA:
Tareas_domesticas = ["2Hacer la comida", "3limpiar la casa", "1hacer la cama"]
Tareas_domesticas.sort()
print(Tareas_domesticas)
def ordenar(Tareas):
    Tareas.sort()
    for indice, i in enumerate(Tareas):
        i = list(i)
        print("Tarea",[indice + 1],":{}".format(i))
        for j in indice:
            if j in i:
                i.remove(j)
                print("Tarea",[indice + 1],":{}".format(i))
            else:
                break 
        
              
print(ordenar(Tareas_domesticas))  
"""


  