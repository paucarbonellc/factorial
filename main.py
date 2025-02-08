import unittest

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El numero debe ser un entero")
    if n < 0:
        raise ValueError("el numero debe ser positivo")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == "__main__":
    unittest.main()
