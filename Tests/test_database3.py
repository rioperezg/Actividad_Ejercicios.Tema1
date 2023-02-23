import csv
import copy
# import config
# import helpers
import unittest
import Database3 as db
class TestDatabase3(unittest.TestCase):
    def setUp1(self):
        db.lista_final = ['h', 'o', 'l', 'a', ' ', 'u', 'n']
    def test_lista_final(self):
        listas_modificadas = db.lista_final(['h', 'o', 'l', 'a', ' ', 'u', 'n'])
        listas_no_modificadas = db.lista_final(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])
        self.assertEqual(listas_modificadas)
        self.assertNotEqual(listas_no_modificadas)