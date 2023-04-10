import unittest
from LargestProductInGrid11 import calcMatrixProd, Direction

class TestCalcMatrixProd(unittest.TestCase):
    def test_calcMatrixProd_left_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 1, 1, Direction.left)
        self.assertEqual(result, 20)

    def test_calcMatrixProd_diagonalUpDx_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 2, 0, Direction.diagonalUpDx)
        self.assertEqual(result, 105)

    def test_calcMatrixProd_diagonalUpSx_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 2, 2, Direction.diagonalUpSx)
        self.assertEqual(result, 45)

    def test_calcMatrixProd_up_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 1, 1, Direction.up)
        self.assertEqual(result, 10)


    def test_calcMatrixProd_down_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 1, 1, Direction.down)
        self.assertEqual(result, 40)

    def test_calcMatrixProd_right_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 1, 1, Direction.right)
        self.assertEqual(result, 30)

    def test_calcMatrixProd_diagonalDownDx_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 0, 0, Direction.diagonalDownDx)
        self.assertEqual(result, 45)

    def test_calcMatrixProd_diagonalDownSx_direction(self):
        matrix = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        result = calcMatrixProd(matrix, 0, 2, Direction.diagonalDownSx)
        self.assertEqual(result, 105)



