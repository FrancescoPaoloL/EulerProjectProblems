import unittest
from LongestCollatzSequence14 import doCollatz

class TestCollatz(unittest.TestCase):

    def test_doCollatz(self):
        self.assertEqual(doCollatz(1), 0)  # the expected result for nrSeq = 1
        self.assertEqual(doCollatz(2), 2)  # the expected result for nrSeq = 2
        self.assertEqual(doCollatz(10), 9)  # the expected result for nrSeq = 10
        self.assertEqual(doCollatz(999999), 837799)  # the expected result for nrSeq = 999999

if __name__ == '__main__':
    unittest.main()
