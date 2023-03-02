import csv
import copy
# import config
# import helpers
import unittest
import Ejercicio_7 as db7
class TestDatabase7(unittest.TestCase):
    def setUp7(self):
        db7.agregar_una_vez = ("Elemento:", 6, "in lista" 
        [1, 2, 5, 6, 23, 2, 3, 'hola'], "Añadido varios elementos")
    def test_setUp7(self):
        lista_actualizada = ("Elemento:", 6, "in lista" 
        [1, 2, 5, 6, 23, 2, 3, 'hola'], "Añadido varios elementos")
        lista_no_actualizada = [1, 2, 5, 6, 23, 2]
        self.assertEqual(lista_actualizada)
        self.assertNotEqual(lista_no_actualizada)