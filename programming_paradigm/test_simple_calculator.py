import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
       self.assertEqual(self.calc.add(2, 3), 5)
       self.assertEqual(self.calc.add(-1, 1), 0)
       self.assertEqual(self.calc.add(-5, 3), -2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-1, -3), -4)
        
    def test_multiplication(self):
       self.assertEqual(self.calc.multiply(5, 2), 10)
       self.assertEqual(self.calc.multiply(2, 2), 4)
       self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_division(self):
       self.assertEqual(self.calc.divide(8, 2), 4)
       self.assertEqual(self.calc.divide(14, 2), 7)
       self.assertEqual(self.calc.divide(2, 2), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(100, 0)

if __name__ == '__main__':
    unittest.main()

        
    
