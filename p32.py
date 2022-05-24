"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of 
the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
from utils import are_equal


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [[0,0,0] for i in range(len(s))]
        for i in range(1, len(s)):
            curr_c = s[i]
            curr_d = dp[i]
            prev_c = s[i-1]
            prev_d = dp[i-1]
            if curr_c == ')':
                if prev_c == '(':
                    prev_d[1] = 1
                    curr_d[0] = prev_d[0]
                    curr_d[1] = 1
                    curr_d[2] = prev_d[2] + 2
                else: # prev_c = ')'
                    if prev_d[1] > 0 and prev_d[0] > 0: # has left parenthesis
                        j = i - prev_d[2] - 1
                        if j >= 0 and s[j] == '(':
                            curr_d[1] = prev_d[1] + 1
                            dp[j][1] = prev_d[1] + 1
                            curr_d[0] = dp[j][0]
                            curr_d[2] = prev_d[2] + dp[j][2] + 2
            else: # curr_c = '('
                if prev_c == '(':
                    curr_d[0] = prev_d[0] + 1
                else: # prev_c = ')'
                    if prev_d[1] > 0:
                        curr_d[0] = prev_d[0]
                        curr_d[2] = prev_d[2]
        
        return max(dp, key=lambda x: x[2])[2] if len(dp) > 0 else 0


def test_solution():
    sol = Solution()
    def test(s: str, expected: int):
        are_equal(sol.longestValidParentheses(s), expected)

    test("", 0)
    test("(()", 2)
    test(")()())", 4)
    test("()(())", 6)
    test("(())", 4)
    test("()(())()", 8)
    test("(()(())())", 10)
    test(")()()))((()(())())))(()))", 12)
    

if __name__ == '__main__':
    test_solution()
