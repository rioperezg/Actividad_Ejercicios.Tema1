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
                

