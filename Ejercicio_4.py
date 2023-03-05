""""
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un 
orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""

def ordenar(Tareas):
    Tareas_ordenadas = [] 
    # Utilizamos el metodo sort para ordenar automaticamente la lista
    Tareas.sort()
    for indice, i in enumerate(Tareas):
        i = list(i)
        # Recorremos esta lista y hacemos de cada elemento cadena de la lista, una lista en si
        for j in i:
            if j == indice:
                # Recorremos estas sublistas y si hay algun elemento en ellas que sea = indice(1,2,3,...) lo borramos
                i.append(j)
            else:
                i.remove(j)        
                break
        # Por ultimo cada sublista la juntamos y convertimos en cadena y añadimos estas cadenas a una lista vacia 
        i = "".join(i)
        Tareas_ordenadas.append(i)
    return Tareas_ordenadas




  