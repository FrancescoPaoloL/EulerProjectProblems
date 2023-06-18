import unittest
from LatticePaths15 import calcMoves

class TestCalcMoves(unittest.TestCase):
    def test_calc_moves(self):
        self.assertEqual(calcMoves(0), 1)
        self.assertEqual(calcMoves(1), 2)
        self.assertEqual(calcMoves(2), 6)
        self.assertEqual(calcMoves(3), 20)
        self.assertEqual(calcMoves(4), 70)

if __name__ == '__main__':
    unittest.main()
