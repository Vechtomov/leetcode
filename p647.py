"""
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


from utils import are_equal

class SolutionSlow:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for l in range(1, len(s)+1):
            for i in range(0, len(s)+1-l):
                is_palindrome = 1
                for j in range(l // 2):
                    if s[i+j] != s[i+l-j-1]:
                        is_palindrome = 0
                        break
                res += is_palindrome
        return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        ld = [{1: True} for i in range(len(s))]
        for l in range(2, len(s)+1):
            for i in range(0, len(s)+1-l):
                if s[i] == s[i+l-1] and (l-2 == 0 or l-2 in ld[i+1]):
                    ld[i][l] = True
                    res += 1
        return res


class SolutionNoMemory:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            j,k = i - 1, i
            while (j>=0 and k < n and (s[j] == s[k])):
                j -= 1
                k += 1
                res += 1
            j,k = i, i
            while (j>=0 and k < n and (s[j] == s[k])):
                j -= 1
                k += 1
                res += 1
        return res

def test():
    s = SolutionNoMemory()
    are_equal(s.countSubstrings('a'), 1)
    are_equal(s.countSubstrings('ab'), 2)
    are_equal(s.countSubstrings('aa'), 3)
    are_equal(s.countSubstrings('aab'), 4)
    are_equal(s.countSubstrings('aba'), 4)
    are_equal(s.countSubstrings('abc'), 3)
    are_equal(s.countSubstrings('aaa'), 6)
    are_equal(s.countSubstrings('aaaa'), 10)
    are_equal(s.countSubstrings('abaa'), 6)
    are_equal(s.countSubstrings('abac'), 5)
    are_equal(s.countSubstrings('ababa'), 9)
    are_equal(s.countSubstrings('abbba'), 9)
    are_equal(s.countSubstrings('abcba'), 7)

if __name__ == '__main__':
    test()