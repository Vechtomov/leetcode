"""
820. Short Encoding of Words
A valid encoding of an array of words is any reference string s and array 
of indices indices such that: words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and 
up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string 
s possible of any valid encoding of words.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].

Constraints:
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""

from typing import List
from utils import are_equal


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        d = {}
        res = 0
        reversed_words = [''.join(reversed(w)) for w in words]
        for w in sorted(reversed_words, reverse=True):
            if w not in d:
                for i in range(len(w)):
                    d[w[:i+1]] = 1

                res += len(w) + 1

        return res


def test_solution():

    def test(words: List[str], expected: int):
        sol = Solution()
        are_equal(sol.minimumLengthEncoding(words), expected)

    test(["a"], 2)
    test(["a", "b"], 4)
    test(["a", "ba"], 3)
    test(["ab", "cd"], 6)
    test(["abcd", "cd"], 5)
    test(["cd", "abcd"], 5)
    test(["abcd", "cd", "cdb"], 9)

    test(["time", "me", "bell"], 10)


if __name__ == '__main__':
    test_solution()
