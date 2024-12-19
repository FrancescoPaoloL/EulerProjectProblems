import unittest
from FactorialDigitSum18 import factorialDigitSum

class TestFactorialDigitSum(unittest.TestCase):
    def test_factorialDigitSum(self):
        self.assertEqual(factorialDigitSum(10), 27)
        self.assertEqual(factorialDigitSum(100), 648)     

        
if __name__ == '__main__':
    unittest.main()

