import csv
import copy
# import config
# import helpers
import unittest
import Database4 as db4
class TestDatabase4(unittest.TestCase):
    def setUp4(self):
        db4.ordenar = ["Hacer la cama", "Hacer la comida", "Limpiar la casa"]
    def test_ordenar(self):
        Tareas_ordenadas = db4.ordenar(["Hacer la cama", "Hacer la comida", "Limpiar la casa"])
        Tareas_NoOrdenadas = db4.ordenar(["2Hacer la comida", "3limpiar la casa", "1hacer la cama"])
        self.assertEqual(Tareas_ordenadas)
        self.assertNotEqual(Tareas_NoOrdenadas)