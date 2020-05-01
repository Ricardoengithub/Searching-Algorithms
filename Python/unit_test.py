import unittest
from secuencial import busquedaSecuencial
from binaria import busquedaBinaria
from exponencial import busquedaExponencial
from interpolacion import busquedaInterpolacion

class BusquedaSecuencialTestCaste(unittest.TestCase):
    def test_busquedaSecuencial(self):
        self.assertEqual(busquedaSecuencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 2)
        self.assertEqual(busquedaSecuencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)
        self.assertEqual(busquedaSecuencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(busquedaSecuencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 97), 24)
        self.assertEqual(busquedaSecuencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 4), -1)
        self.assertEqual(busquedaSecuencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 11), 4)
        self.assertEqual(busquedaSecuencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 2), 0)

class BusquedaBinariaTestCase(unittest.TestCase):
    def test_busquedaBinaria(self):
        self.assertEqual(busquedaBinaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 2)
        self.assertEqual(busquedaBinaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)
        self.assertEqual(busquedaBinaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(busquedaBinaria([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 97), 24)
        self.assertEqual(busquedaBinaria([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 4), -1)
        self.assertEqual(busquedaBinaria([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 11), 4)
        self.assertEqual(busquedaBinaria([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 2), 0)

class BusquedaExponencialTestCase(unittest.TestCase):

    def test_busquedaExponencial(self):
        self.assertEqual(busquedaExponencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 3), 2)
        self.assertEqual(busquedaExponencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 8), 7)
        self.assertEqual(busquedaExponencial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 16, 11), -1)
        self.assertEqual(busquedaExponencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 32, 97), 24)
        self.assertEqual(busquedaExponencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 4, 4), -1)
        self.assertEqual(busquedaExponencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 8, 11), 4)
        self.assertEqual(busquedaExponencial([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 1, 2), 0)

class BusquedaInterpolacionTestCase(unittest.TestCase):

    def test_busquedaInterpolacion(self):
        self.assertEqual(busquedaInterpolacion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 2)
        self.assertEqual(busquedaInterpolacion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)
        self.assertEqual(busquedaInterpolacion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(busquedaInterpolacion([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 97), 24)
        self.assertEqual(busquedaInterpolacion([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 4), -1)
        self.assertEqual(busquedaInterpolacion([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 11), 4)
        self.assertEqual(busquedaInterpolacion([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 2), 0)


if __name__ == '__main__':
    unittest.main() 

