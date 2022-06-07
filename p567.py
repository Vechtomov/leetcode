"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""

from utils import are_equal
from typing import List
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        symbols = Counter(s1)
        curr_symbols = defaultdict(int)
        sym_sum = sum(symbols.values())
        curr_sum = 0
        for i, c in enumerate(s2):
            if i >= len(s1):
                old_c = s2[i - len(s1)]
                if old_c in symbols:
                    curr_symbols[old_c] -= 1
                    if curr_symbols[old_c] < symbols[old_c]:
                        curr_sum -= 1

            if c in symbols:
                curr_symbols[c] += 1
                if curr_symbols[c] <= symbols[c]:
                    curr_sum += 1
                if curr_sum == sym_sum:
                    return True

        return False


def test_solution():
    sol = Solution()

    def test(s1: str, s2: str, expected: bool):
        are_equal(sol.checkInclusion(s1, s2), expected)

    test("a", "a", True)
    test("a", "b", False)
    test("a", "aa", True)
    test("ab", "ab", True)
    test("ab", "cab", True)
    test("ab", "ccbcbbaccb", True)
    test("abb", "abb", True)
    test("abb", "bab", True)
    test("abb", "aab", False)
    test("abb", "bba", True)
    test("abb", "aaabaaab", False)
    test("abb", "aaababaab", True)
    test("abbc", "adbcabde", True)
    test("abbc", "cbcabde", True)
    test("abbc", "cbcab", True)
    test("abbc", "ccbcab", True)
    test("abbc", "ccbcabde", True)
    test("abbc", "cccbcabde", True)
    test("abbc", "cccdbcabde", True)
    test("abbc", "aaadabcabde", True)
    test("abbc", "aaababcabde", True)
    test("ab", "eidbaooo", True)
    test("ab", "eidboaoo", False)


if __name__ == '__main__':
    test_solution()
