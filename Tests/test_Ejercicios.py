import unittest
import Ejercicio_1 as E1
import Ejercicio_2 as E2
import Ejercicio_3 as E3
import Ejercicio_4 as E4
import Descomposicion as db5
import Ejercicio_6 as E6
import Ejercicio_7 as E7

class TestDatabase1(unittest.TestCase):
    def setUp1(self):
        E1.nombre_y_apellidos.__init__= "zereP nauJ, 01"
    def test_cadena(self):
        cadena_modificada = E1.nombre_y_apellidos.Cadena("Juan Perez ha sacado un 10")
        cadena_no_modificada = E1.nombre_y_apellidos.Cadena("zereP nauJ, 01")
        self.assertIsNotNone(cadena_modificada)
        self.assertIsNone(cadena_no_modificada)
class TestDatabase2(unittest.TestCase):
    def setUp2(self):
        E2.numero_final.__init__= 4
    def test_operacion(self):
        numero_obtenido = E2.numero_final.operacion(444444444)
        numero_noObtenido = E2.numero_final.operacion(4)
        self.assertEqual(numero_obtenido)
        self.assertNotEqual(numero_noObtenido)
class TestDatabase3(unittest.TestCase):
    def setUp3(self):
        E3.lista_final = ['h', 'o', 'l', 'a', ' ', 'u', 'n']
    def test_lista_final(self):
        listas_modificadas = E3.lista_final(['h', 'o', 'l', 'a', ' ', 'u', 'n'])
        listas_no_modificadas = E3.lista_final(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])
        self.assertEqual(listas_modificadas)
        self.assertNotEqual(listas_no_modificadas)
class TestDatabase4(unittest.TestCase):
    def setUp4(self):
        E4.ordenar = ["Hacer la cama", "Hacer la comida", "Limpiar la casa"]
    def test_ordenar(self):
        Tareas_ordenadas = E4.ordenar(["Hacer la cama", "Hacer la comida", "Limpiar la casa"])
        Tareas_NoOrdenadas = E4.ordenar(["2Hacer la comida", "3limpiar la casa", "1hacer la cama"])
        self.assertEqual(Tareas_ordenadas)
        self.assertNotEqual(Tareas_NoOrdenadas)
class TestDatabase5(unittest.TestCase):
    def setUp5(self):
        db5.Descomposicion = ("000008")
        ("000070")
        ("000600")
        ("003000")
        ("020000")
        ("100000")
    def test_Descomposicion(self):
        numero_descompuesto = db5.Descomposicion(("000008")
                             ("000070")
                             ("000600")
                             ("003000")
                             ("020000")
                             ("100000"))
        numero_sin_descomponer = db5.Descomposicion(123678)
        self.assertEqual(numero_descompuesto)
        self.assertNotEqual(numero_sin_descomponer) 
class TestDatabase6(unittest.TestCase):
    def setUp6(self):
        E6.Separar = "Estos son los numeros pares:" [42, 56, 18, 76], "y estos son los numeros impares:" [23, 35, 81]
    def test_Separar(self): 
        Lista_separada = E6.Separar("Estos son los numeros pares:" [42, 56, 18, 76], "y estos son los numeros impares:" [23, 35, 81])
        Lista_no_separada = E6.Separar([23,42,56,18,35,76,81])
        self.assertEqual(Lista_separada)
        self.assertNotEqual(Lista_no_separada)        
class TestDatabase7(unittest.TestCase):
    def setUp7(self):
        E7.agregar_una_vez = ("Elemento:", 6, "in lista" 
        [1, 2, 5, 6, 23, 2, 3, 'hola'], "Añadido varios elementos")
    def test_setUp7(self):
        lista_actualizada = E7.agregar_una_vez("Elemento:", 6, "in lista" 
        [1, 2, 5, 6, 23, 2, 3, 'hola'], "Añadido varios elementos")
        lista_no_actualizada = E7.agregar_una_vez([1, 2, 5, 6, 23, 2])
        self.assertEqual(lista_actualizada)
        self.assertNotEqual(lista_no_actualizada)