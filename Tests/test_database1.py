import csv
import copy
# import config
# import helpers
import unittest
import Ejercicio_1 as db1

class TestDatabase1(unittest.TestCase):
    def setUp1(self):
        db1.nombre_y_apellidos.__init__= "zereP nauJ, 01"
    def test_cadena(self):
        cadena_modificada = db1.nombre_y_apellidos.Cadena("Juan Perez ha sacado un 10")
        cadena_no_modificada = db1.nombre_y_apellidos.Cadena("zereP nauJ, 01")
        self.assertIsNotNone(cadena_modificada)
        self.assertIsNone(cadena_no_modificada)