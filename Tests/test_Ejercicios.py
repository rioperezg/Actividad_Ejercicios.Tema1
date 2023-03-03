import unittest
import Ejercicio_1 as E1
import Ejercicio_2 as E2
import Ejercicio_3 as E3
import Ejercicio_4 as E4
import Descomposicion as db5
import Ejercicio_6 as E6
import Ejercicio_7 as E7

class TestDatabase1(unittest.TestCase):
    def test_cadena(self):
        cadena_modificar = E1.Cadena("zereP nauJ,01")
        self.assertEqual(cadena_modificar, "Juan Perez ha sacado un 10")

    def test_operacion(self):
        numero_aobtener = E2.operacion(4)
        self.assertEqual(numero_aobtener, "Finalmente, el numero que resulta de multiplicar 12345679 y 36 es: 444444444")

    def test_lista_final(self):
        listas_modificadas = E3.lista_final(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])
        self.assertEqual(listas_modificadas, ['h', 'o', 'l', 'a', ' ', 'u', 'n'])

    def test_ordenar(self):
        Tareas_ordenadas = E4.ordenar(["2Hacer la comida", "3Limpiar la casa", "1Hacer la cama"])
        self.assertEqual(Tareas_ordenadas, ["Hacer la cama", "Hacer la comida", "Limpiar la casa"])
        
    def test_Separar(self): 
        Lista_separada = E6.Separar([23,42,56,18,35,76,81])
        self.assertEqual(Lista_separada, "Estos son los numeros pares: [42, 56, 18, 76], y estos son los numeros impares: [23, 35, 81]")       
 
    def test_agregar(self):
        lista_actualizada = E7.agregar_una_vez([1, 2, 5, 6, 23, 2], [3, 6, "hola"])
        self.assertEqual(lista_actualizada, "Elemento:6, in lista"
"[1, 2, 5, 6, 23, 2, 3, 'hola'] Añadido varios elementos")  
"""" 
    def test_Descomposicion(self):
        numero_descompuesto = db5.Descomposicion(123678)
        self.assertEqual(numero_descompuesto, 
                        000008
                        000070
                        000600
                        003000
                        020000
                        100000)
"""
