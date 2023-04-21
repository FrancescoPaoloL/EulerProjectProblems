import unittest
from PowerDigitSum16 import SumOfDigits

class TestSumOfDigits(unittest.TestCase):
    def test_small_exp(self):
        self.assertEqual(SumOfDigits(15), 26)
       
    def test_zero_exp(self):
        self.assertEqual(SumOfDigits(0), 1)
        
    def test_negative_exp(self):
        self.assertRaises(ValueError, SumOfDigits, -5)

    def test_large_exp(self):
        self.assertEqual(SumOfDigits(1000), 1366)

if __name__ == '__main__':
    unittest.main()
