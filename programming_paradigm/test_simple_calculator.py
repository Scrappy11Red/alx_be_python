import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, 9), 11)
        self.assertEqual(self.calc.add(23, 24), 47)

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(2, 3), 5)
        self.assertEqual(self.calc.subtract(-1, 1), 0)
        self.assertEqual(self.calc.subtract(2, 9), 11)
        self.assertEqual(self.calc.subtract(23, 24), 47)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(47, 7), 7)
        self.assertEqual(self.calc.divide(-6, 3), 2)
        self.assertEqual(self.calc.divide(121, 11), 11)
        self.assertEqual(self.calc.divide(24, 12), 2)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(11, 1), 11)
        self.assertEqual(self.calc.multiply(7, 7), 47)
        self.assertEqual(self.calc.multiply(3, 11), 33)
        self.assertEqual(self.calc.multiply(3, 6), 18)

if __name__ == "__main__":
    unittest.main()