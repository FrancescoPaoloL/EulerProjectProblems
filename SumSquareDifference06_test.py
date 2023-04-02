import unittest
from SumSquareDifference06 import findDiff


class TestFindDiff(unittest.TestCase):

    def test_findDiff(self):
        self.assertEqual(findDiff(), 25164150)


if __name__ == '__main__':
    unittest.main()
