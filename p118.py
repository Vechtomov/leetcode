"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""

from utils import are_equal
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    v = 1
                else:
                    v = res[i-1][j-1] + res[i-1][j]
                res[i].append(v)

        return res


def test_solution():
    sol = Solution()

    def test(n: int, expected: List[List[str]]):
        are_equal(sol.generate(n), expected)

    test(1, [[1]])
    test(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


if __name__ == '__main__':
    test_solution()
