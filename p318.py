"""
318. Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

Constraints:
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""

from typing import List
from utils import are_equal
from itertools import combinations


class SolutionNaive:
    def maxProduct(self, words: List[str]) -> int:
        m = 0
        ws = [(len(w), set(w)) for w in words]
        for c in combinations(ws, 2):
            if not c[0][1] & c[1][1]:
                m = max(m, c[0][0] * c[1][0])
        return m


class SolutionBitMask:
    def maxProduct(self, words: List[str]) -> int:
        masks = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            masks[mask] = max(masks.get(mask, 0), len(w))
        return max([masks[x] * masks[y] for x in masks for y in masks if not x & y] or [0])


def test_solution():
    s = SolutionBitMask()

    def test(words: List[str], expected: int):
        are_equal(s.maxProduct(words), expected)

    test(["a", "aa"], 0)
    test(["a", "b"], 1)
    test(["a", "bc"], 2)
    test(["a", "bcd"], 3)
    test(["a", "abc"], 0)
    test(["ab", "cd"], 4)
    test(["ab", "ac", "bc", "cd"], 4)
    test(["ab", "cd", "efg"], 6)
    test(["a", "aa", "aaa", "aaaa"], 0)
    test(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16)
    test(["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4)


if __name__ == '__main__':
    test_solution()
