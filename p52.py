"""
52. N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such 
that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""

from utils import are_equal
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens: List[int], xy_diff: List[int], xy_sum: List[int]):
            i = len(queens)
            if i == n:
                return 1
            res = 0
            for j in range(n):
                if j not in queens and (i-j) not in xy_diff and (i+j) not in xy_sum:
                    res += dfs(queens + [j], xy_diff + [i-j], xy_sum + [i+j])
            return res

        return dfs([], [], [])


def test_solution():
    sol = Solution()

    def test(n: int, expected: List[List[str]]):
        are_equal(sol.totalNQueens(n), expected)

    test(1, 1)
    test(2, 0)
    test(3, 0)
    test(4, 2)
    print(sol.totalNQueens(5))
    print(sol.totalNQueens(6))
    print(sol.totalNQueens(7))
    print(sol.totalNQueens(8))
    print(sol.totalNQueens(9))


if __name__ == '__main__':
    test_solution()
