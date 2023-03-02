import csv
import copy
# import config
# import helpers
import unittest
import Ejercicio_2 as db2
class TestDatabase2(unittest.TestCase):
    def setUp2(self):
        db2.numero_final.__init__= 4
    def test_operacion(self):
        numero_obtenido = db2.numero_final.operacion(444444444)
        numero_noObtenido = db2.numero_final.operacion(4)
        self.assertEqual(numero_obtenido)
        self.assertNotEqual(numero_noObtenido)
    
