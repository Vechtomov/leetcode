"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

from typing import List
from utils import are_equal


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(s, l, r):
            i = l + r
            if l > n:
                return
            if i == 2*n and l == r:
                res.append(s)
                return
            generate(s + '(', l + 1, r)
            if r < l:
                generate(s + ')', l, r + 1)

        generate('(', 1, 0)
        return res


def test_solution():
    s = Solution()
    def test(n: int, expected: List[str]):
        are_equal(set(s.generateParenthesis(n)), set(expected))

    test(1, ["()"])
    test(2, ["(())", "()()"])
    test(3, ["((()))","(()())","(())()","()(())","()()()"])


if __name__ == '__main__':
    test_solution()
