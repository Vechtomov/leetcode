"""
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to 
either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""

from utils import are_equal
from typing import List


class SolutionTopDown:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}

        def helper(row: int, col: int) -> int:
            if row == len(triangle) - 1:
                return triangle[row][col]

            next_row = row + 1
            left = dp[(next_row, col)] if (
                next_row, col) in dp else helper(next_row, col)
            right = dp[(next_row, col+1)] if (next_row, col +
                                              1) in dp else helper(next_row, col + 1)
            result = min(left, right) + triangle[row][col]
            dp[(row, col)] = result
            return result

        return helper(0, 0)


class SolutionBottomUp:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[0] * (rows+1) for _ in range(rows+1)]

        for row in range(rows - 1, -1, -1):
            for col in range(row+1):
                dp[row][col] = min(dp[row+1][col],
                                   dp[row+1][col+1]) + triangle[row][col]

        return dp[0][0]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        acc = [float('inf')] * (rows + 1)
        acc[1] = triangle[0][0]
        for row in range(1, rows):
            for col in range(row+1, 0, -1):
                acc[col] = min(acc[col], acc[col-1]) + triangle[row][col-1]

        return min(acc)


def test_solution():
    sol = Solution()

    def test(triangle: List[List[int]], expected: int):
        are_equal(sol.minimumTotal(triangle), expected)

    test([[1]], 1)
    test([[1], [1, 3]], 2)
    test([[1], [3, 1]], 2)
    test([[1], [3, 1], [1, 6, 7]], 5)

    test([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11)
    test([[-10]], -10)


if __name__ == '__main__':
    test_solution()
