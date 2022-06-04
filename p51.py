"""
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""

from utils import are_equal
from typing import List, Tuple
import numpy as np

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_new_board(board: np.ndarray, i, j):
            new_board = board.copy()
            for k in range(i+1, n):
                new_board[k, j] = 1
                offset = k - i
                if j + offset < n:
                    new_board[k, j + offset] = 1
                if j - offset >= 0:
                    new_board[k, j - offset] = 1
            return new_board

        def get_queens(board: np.ndarray, i: int) -> List[List[Tuple[int]]]:
            res = []
            for j in range(n):
                if not board[i, j]:
                    b = get_new_board(board, i, j)
                    if i < n - 1:
                        solutions = get_queens(b, i + 1)
                        for sol in solutions:
                            sol.append((i, j))
                            res.append(sol)
                    else:
                        res.append([(i,j)])
            return res

        board = np.zeros((n,n))
        solutions = get_queens(board, 0)
        result = []
        for sol in solutions:
            temp = [['.'] * n for _ in range(n)]
            for i,j in sol:
                temp[i][j] = 'Q'
                temp[i] = ''.join(temp[i])
            result.append(temp)
        return result


def test_solution():
    sol = Solution()

    def test(n: int, expected: List[List[str]]):
        are_equal(sol.solveNQueens(n), expected)

    test(1, [["Q"]])
    test(2, [])
    test(3, [])
    test(4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
    print(sol.solveNQueens(5))
    print(sol.solveNQueens(6))
    print(sol.solveNQueens(7))
    print(sol.solveNQueens(8))
    print(sol.solveNQueens(9))


if __name__ == '__main__':
    test_solution()
