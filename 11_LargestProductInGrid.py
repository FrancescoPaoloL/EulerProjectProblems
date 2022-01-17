'''
In the 20x20 grid below, four numbers along a diagonal line 
have been marked in red.

see: ...
        26
           63
              78
                 14

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the 
same direction (up, down, left, right, or diagonally) in the 
20x20 grid?

---
We have a matrix: 20x20



We have 5 directions (Every direction check matrix limit!):
- up: row: actual position - 1, 2, 3: col: same index    chk row
- down: row: actual position + 1, 2, 3; col = same index  chk row
- left: row: actual position, col - 1, 2, 3         chk col
- right: row: actual position, col + 1, 2, 3        chk col
- diagonally: loop
               row: actual + 1, 2, 3; col: actual + 1, 2, 3


ANS = 70600674 --> 70600674
'''

import time
import enum


print('Start!')
start_time = time.time()

class MaxNr():
    value = 0

  
# creating enumerations using class
class Direction(enum.Enum):
    up = 1
    down = 2
    left = 3
    right = 4
    diagonalDownDx = 5
    diagonalDownSx = 6
    diagonalUpDx = 7
    diagonalUpSx = 8


kLimit = 19
kOffset = 4


def calcMatrixProd(matrix, row, col, direction):
    tmp = 1
    offsetRow = row
    offsetCol = col
    for idx in range(0, kOffset):
        if direction == Direction.up:
            offsetRow = row - idx
        elif direction == Direction.down:
            offsetRow = row + idx
        elif direction == Direction.left:
            offsetCol = col - idx
        elif direction == Direction.right:
            offsetCol = col + idx      
        elif direction == Direction.diagonalDownDx:
            offsetRow = row + idx
            offsetCol = col + idx
        elif direction == Direction.diagonalDownSx:
            offsetRow = row + idx
            offsetCol = col - idx
        elif direction == Direction.diagonalUpDx:
            offsetRow = row - idx
            offsetCol = col + idx
        elif direction == Direction.diagonalUpSx:
            offsetRow = row - idx
            offsetCol = col - idx

        if offsetRow > kLimit or offsetRow < 0:
            break
        if offsetCol > kLimit or offsetCol < 0:
            break

        tmp *= int(matrix[offsetRow][offsetCol])
        if tmp > MaxNr.value:
            MaxNr.value = tmp
    return tmp

matrix = [
            ['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08'],
            ['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00'],
            ['81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65'],
            ['52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91'],
            ['22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80'],
            ['24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50'],
            ['32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70'],
            ['67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21'],
            ['24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72'],
            ['21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95'],
            ['78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92'],
            ['16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57'],
            ['86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58'],
            ['19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40'],
            ['04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66'],
            ['88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69'],
            ['04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36'],
            ['20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16'],
            ['20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54'],
            ['01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']
        ]

# matrix = [
#             ['08', '02', '22', '97', '38', '15'],
#             ['49', '49', '99', '40', '17', '81'],
#             ['81', '49', '31', '73', '55', '79'],
#             ['52', '70', '95', '23', '04', '60'],
#             ['22', '31', '16', '71', '51', '67'],
#             ['24', '47', '32', '60', '99', '03']
#         ]

# t = calcMatrixProd(matrix, 0, 0, Direction.down) # -> 1651104
# t = calcMatrixProd(matrix, 0, 0, Direction.up) # -> 8
# t = calcMatrixProd(matrix, 0, 0, Direction.left) # -> 8
# t = calcMatrixProd(matrix, 0, 0, Direction.right) # -> 34144
# t = calcMatrixProd(matrix, 0, 0, Direction.diagonalDownSx) # -> 8
# t = calcMatrixProd(matrix, 0, 0, Direction.diagonalUpDx) # -> 8
# t = calcMatrixProd(matrix, 0, 0, Direction.diagonalDownDx) # -> 279496
# t = calcMatrixProd(matrix, 0, 0, Direction.diagonalUpSx) # -> 8


for row in range(kLimit):
    for col in range(kLimit):
        calcMatrixProd(matrix, row, col, Direction.down)
        calcMatrixProd(matrix, row, col, Direction.up)
        calcMatrixProd(matrix, row, col, Direction.left)
        calcMatrixProd(matrix, row, col, Direction.right)
        calcMatrixProd(matrix, row, col, Direction.diagonalDownSx)
        calcMatrixProd(matrix, row, col, Direction.diagonalUpDx)
        calcMatrixProd(matrix, row, col, Direction.diagonalDownDx)
        calcMatrixProd(matrix, row, col, Direction.diagonalUpSx)

print(f'The greatest product of {kOffset} adjacent numbers is {MaxNr.value}')
print("--- %s seconds ---" % (time.time() - start_time))


''''''''''''

# rows, cols = 20, 20
# matrix = [([0]*cols) for i in range(rows)]
