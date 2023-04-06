import unittest
from PythagoreanTriplet09 import PythagoreanTriplets


class TestPythagoreanTriplets(unittest.TestCase):
    def test_triplet_sum_1000(self):
        a, b, c = PythagoreanTriplets()
        self.assertEqual(a**2 + b**2, c**2)
        self.assertEqual(a + b + c, 1000)

if __name__ == '__main__':
    unittest.main()
