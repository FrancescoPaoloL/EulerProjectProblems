import unittest
from Palindrome4Digits04 import find_largest_palindrome

class TestFindLargestPalindrome(unittest.TestCase):
    
    def test_result_type(self):
        result = find_largest_palindrome()
        self.assertIsInstance(result, int, "Function should return an integer")
        
    def test_result_value(self):
        result = find_largest_palindrome()
        self.assertEqual(result, 906609, "Result should be 906609")

if __name__ == '__main__':
    unittest.main()
