""""
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un 
orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""
#Mi idea es predefinir un diccionario con el orden ya establecido. Y con el metodo sort ordenar todas las tareas de mayor a menor 
#importancia de acuerdo al numero que estan asignados. no, tenemos que hacerlo de forma diferente
Tareas_Domesticas = ["2Recoger los platos", "1Hacer la cama", "3Hacer la comida"]
    

def ordenar(Tareas):
    Tareas_ordenadas = Tareas.sort()
    for tarea in enumerate(Tareas_ordenadas):
        tarea = list(tarea)
        return tarea          
print(ordenar(Tareas_Domesticas))         


  