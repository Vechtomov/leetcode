"""
304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined 
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the 
elements of matrix inside the rectangle defined by its upper left corner 
(row1, col1) and lower right corner (row2, col2).

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]
Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion.

1 2 3
4 5 6
7 8 9

"""

from utils import are_equal
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cum_sum_matrix = self._calc_cum_sum_matrix(matrix)

    def _calc_cum_sum_matrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        res = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                res[i][j] = res[i-1][j] + res[i][j-1] + matrix[i-1][j-1] - res[i-1][j-1]
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cum_sum_matrix[row2+1][col2+1] \
                - self.cum_sum_matrix[row1][col2+1] \
                - self.cum_sum_matrix[row2+1][col1] \
                + self.cum_sum_matrix[row1][col1]


def test_solution():

    def test(matrix: List[List[int]], commands: List[List[int]], expected: List[int]):
        sol = NumMatrix(matrix)
        for comm, expect in zip(commands, expected):
            are_equal(sol.sumRegion(*comm), expect)

    """
    1 2 3
    4 5 6
    7 8 9
    """
    test(
        [[1,2,3], [4,5,6], [7,8,9]], 
        [[0,0,0,0], [0,0,1,1], [1,1,2,2]], 
        [1, 12, 28])
    test(
        [[3,0,1,4,2], [5,6,3,2,1], [1,2,0,1,5], [4,1,0,1,7], [1,0,3,0,5]], [[2,1,4,3],
        [1,1,2,2], [1,2,2,4]], 
        [8, 11, 12])


if __name__ == '__main__':
    test_solution()
