import unittest
from SmallestMultiple05 import smallestNr


class TestSmallestNr(unittest.TestCase):

    def test_smallestNr(self):
        self.assertEqual(smallestNr(), 232792560)


if __name__ == '__main__':
    unittest.main()
