import csv
import copy
# import config
# import helpers
import unittest
import Descomposicion as db5
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
                         