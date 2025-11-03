import unittest

# Funciones que vamos a probar
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


# Clase de prueba
class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(0, 3), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 2), 8)
        self.assertEqual(multiplicar(-1, 5), -5)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == '__main__':
    unittest.main()
