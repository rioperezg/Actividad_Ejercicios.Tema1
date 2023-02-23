import csv
import copy
# import config
# import helpers
import unittest
import Database1 as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.nombre_y_apellidos.__init__ = "zereP nauJ, 01"
    def test_cadena(self):
        cadena_modificada = db.nombre_y_apellidos.Cadena("Juan Perez ha sacado un 10")
        cadena_no_modificada = db.nombre_y_apellidos.Cadena("zereP nauJ, 01")
        self.assertIsNotNone(cadena_modificada)
        self.assertIsNone(cadena_no_modificada)