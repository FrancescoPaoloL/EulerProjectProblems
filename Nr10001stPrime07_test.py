import unittest
from Nr10001stPrime07 import findNrPrime


class TestFindNrPrime(unittest.TestCase):

    def test_findNrPrime(self):
        self.assertEqual(findNrPrime(), (104743, 10001))


if __name__ == '__main__':
    unittest.main()
