import unittest
from HighlyDivisibleTriangularNr12 import factor_count, f

class TestFunctions(unittest.TestCase):
    def test_factor_count(self):
        self.assertEqual(factor_count(1), 1)
        self.assertEqual(factor_count(2), 2)
        self.assertEqual(factor_count(3), 2)
        self.assertEqual(factor_count(6), 4)
    
    def test_f(self):
        self.assertEqual(f(0), 1)
        self.assertEqual(f(1), 3)
        self.assertEqual(f(2), 6)
        self.assertEqual(f(3), 6)
        self.assertEqual(f(500), 76576500)

if __name__ == '__main__':
    unittest.main()