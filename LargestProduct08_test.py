import unittest
from LargestProduct08 import findDigits

class TestFindDigits(unittest.TestCase):
    def test_findDigits_single_digit(self):
        digits = '1'
        group = 1
        expected_seq = '1'
        expected_mul = 1
        seq, mul = findDigits(digits, group)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(mul, expected_mul)

    def test_findDigits_duplicate_digits(self):
        digits = '2222'
        group = 2
        expected_seq = '22'
        expected_mul = 4
        seq, mul = findDigits(digits, group)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(mul, expected_mul)

    def test_findDigits_large_group(self):
        digits = '123456789'
        group = 9
        expected_seq = '123456789'
        expected_mul = 362880
        seq, mul = findDigits(digits, group)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(mul, expected_mul)

if __name__ == '__main__':
    unittest.main()
