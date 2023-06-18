import unittest
from problemSpecialNumbers01 import listSpecialNumbers

class TestListSpecialNumbers(unittest.TestCase):
    
    def setUp(self):
        self.special_numbers = listSpecialNumbers()
    
    def test_special_numbers_are_unique(self):
        self.assertSetEqual(set(self.special_numbers), set(range(3, 1000, 3)) | set(range(5, 1000, 5)))
    
    def test_special_numbers_sum_is_correct(self):
        self.assertEqual(sum(self.special_numbers), 233168)
