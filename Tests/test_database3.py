import csv
import copy
# import config
# import helpers
import unittest
import Ejercicio_3 as db3
class TestDatabase3(unittest.TestCase):
    def setUp3(self):
        db3.lista_final = ['h', 'o', 'l', 'a', ' ', 'u', 'n']
    def test_lista_final(self):
        listas_modificadas = db3.lista_final(['h', 'o', 'l', 'a', ' ', 'u', 'n'])
        listas_no_modificadas = db3.lista_final(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])
        self.assertEqual(listas_modificadas)
        self.assertNotEqual(listas_no_modificadas)