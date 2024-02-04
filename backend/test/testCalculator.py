import unittest
from calculator import Calculator
import math
class TestCalculator(unittest.TestCase):
    def test_calculate_valid_expression(self):
        calculator = Calculator()
        result = calculator.calculate("3 4 + 5 *")
        self.assertEqual(result, 35)

    def test_calculate_invalid_expression(self):
        calculator = Calculator()
        with self.assertRaises(ValueError):
            calculator.calculate("3 +")  # Invalid expression

    def test_calculate_division_by_zero(self):
        calculator = Calculator()
        result = calculator.calculate("3 0 /")  # Division by zero
        self.assertTrue(math.isnan(result))
        calculator.calculate("3 0 /")  # Division by zero

if __name__ == '__main__':
    unittest.main()
