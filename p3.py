"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from utils import are_equal


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        max_len, cur_len = 0, 0
        for i, c in enumerate(s):
            cur_len = min(cur_len + 1, i - dp.get(c, -1))
            max_len = max(max_len, cur_len)
            dp[c] = i
        return max_len


def test_solution():
    sol = Solution()

    def test(s: str, expected: int):
        are_equal(sol.lengthOfLongestSubstring(s), expected)

    test("", 0)
    test("a", 1)
    test("aa", 1)
    test("aaa", 1)
    test("ab", 2)
    test("aba", 2)
    test("abc", 3)
    test("abca", 3)
    test("abac", 3)
    test("abcabcbb", 3)
    test("pwwkew", 3)


if __name__ == '__main__':
    test_solution()
