import csv
import copy
# import config
# import helpers
import unittest
import Database6 as db6
class TestDatabase6(unittest.TestCase):
    def setUp6(self):
        db6.Separar = "Estos son los numeros pares:" [42, 56, 18, 76], "y estos son los numeros impares:" [23, 35, 81]
    def test_Separar(self): 
        Lista_separada = db6.Separar("Estos son los numeros pares:" [42, 56, 18, 76], "y estos son los numeros impares:" [23, 35, 81])
        Lista_no_separada = db6.Separar([23,42,56,18,35,76,81])
        self.assertEqual(Lista_separada)
        self.assertNotEqual(Lista_no_separada)