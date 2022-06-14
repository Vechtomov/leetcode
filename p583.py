"""
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps 
required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""

from utils import are_equal
from typing import List


class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0] * (len(w2)+1) for _ in range(len(w1)+1)]

        for i in range(1, len(w1) + 1):
            for j in range(1, len(w2) + 1):
                v = int(w1[i-1] == w2[j-1])
                dp[i][j] = max(dp[i-1][j-1] + v, dp[i-1][j], dp[i][j-1])

        return len(w1) + len(w2) - dp[len(w1)][len(w2)] * 2

def test_solution():
    sol = Solution()

    def test(w1: str, w2: str, expected: str):
        are_equal(sol.minDistance(w1, w2), expected)

    test("a", "b", 2)
    test("a", "a", 0)
    test("aba", "baa", 2)
    test("aba", "baa", 2)
    test("abcadaca", "baadac", 4)

    test("sea", "eat", 2)
    test("leetcode", "etco", 4)


if __name__ == '__main__':
    test_solution()
